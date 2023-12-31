from concurrent import futures
import grpc
import smart_home_pb2
import smart_home_pb2_grpc
import time
import random
import pika
import json

# RabbitMQ
# Configurações do RabbitMQ
rabbitmq_host = 'localhost'

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

class ClientService(smart_home_pb2_grpc.ClientServiceServicer):
    def SetActuatorValues(self, request, context):
        actuator_type = request.type
        value = request.value
        response = []

        if actuator_type == smart_home_pb2.LAMP:
            try:
                with grpc.insecure_channel('localhost:50053') as channel:
                    stub = smart_home_pb2_grpc.LampServiceStub(channel)
                    state = True if value == "ON" else False
                    obj_res = stub.SetState(smart_home_pb2.LampRequest(state=state))
                    response.append(smart_home_pb2.ObjectValue(type="status", value=value))
            except Exception as e:
                response.append(smart_home_pb2.ObjectValue(type="error", value=""))
        elif actuator_type == smart_home_pb2.THERMOSTAT:
            try:
                with grpc.insecure_channel('localhost:50052') as channel:
                    stub = smart_home_pb2_grpc.ThermostatServiceStub(channel)
                    obj_res = stub.UpdateDesiredTemperature(smart_home_pb2.TemperatureRequest(temperature=float(value)))
                    response.append(smart_home_pb2.ObjectValue(type="temperature", value=value))
            except Exception as e:
                response.append(smart_home_pb2.ObjectValue(type="error", value=""))          
        elif actuator_type == smart_home_pb2.IRRIGATOR:
            try:
                with grpc.insecure_channel('localhost:50054') as channel:
                    stub = smart_home_pb2_grpc.IrrigatorServiceStub(channel)
                    state = True if value == "ON" else False
                    obj_res = stub.SetStateIrrigator(smart_home_pb2.IrrigatorRequest(state=state))
                    response.append(smart_home_pb2.ObjectValue(type="status", value=value))
            except Exception as e:
                print(e)
                response.append(smart_home_pb2.ObjectValue(type="error", value=""))
        else:
            response.append(smart_home_pb2.ObjectValue(type="error", value="Objeto não existe"))

        return smart_home_pb2.ObjectResponse(values=response)
    
    def GetActuatorValues(self, request, context):
        actuator_type = request.type
        response = []

        if actuator_type == smart_home_pb2.LAMP:
            try:
                with grpc.insecure_channel('localhost:50053') as channel:
                    stub = smart_home_pb2_grpc.LampServiceStub(channel)
                    obj_res = stub.GetState(smart_home_pb2.Empty())
                    state = "ON" if obj_res.success == True else "OFF"
                    response.append(smart_home_pb2.ObjectValue(type="status", value=state))
            except Exception as e:
                response.append(smart_home_pb2.ObjectValue(type="error", value=""))
        elif actuator_type == smart_home_pb2.THERMOSTAT:
            try:
                with grpc.insecure_channel('localhost:50052') as channel:
                    stub = smart_home_pb2_grpc.ThermostatServiceStub(channel)
                    obj_res = stub.GetTemperature(smart_home_pb2.Empty())
                    response.append(smart_home_pb2.ObjectValue(type="temperature", value=f"{obj_res.temperature}"))
            except Exception as e:
                response.append(smart_home_pb2.ObjectValue(type="error", value=""))
        elif actuator_type == smart_home_pb2.IRRIGATOR:
            try:
                with grpc.insecure_channel('localhost:50054') as channel:
                    stub = smart_home_pb2_grpc.IrrigatorServiceStub(channel)
                    obj_res = stub.GetStateIrrigator(smart_home_pb2.Empty())
                    state = "ON" if obj_res.success == True else "OFF"
                    response.append(smart_home_pb2.ObjectValue(type="status", value=state))
            except Exception as e:
                response.append(smart_home_pb2.ObjectValue(type="error", value=""))
        else:
            response.append(smart_home_pb2.ObjectValue(type="error", value="Objeto não existe"))
        
        return smart_home_pb2.ObjectResponse(values=response)

    def GetSensorValues(self, request, context):
        sensor_type = request.type

        while context.is_active():
            response = []
            
            method_frame, header_frame, body = channel.basic_get(queue='sensor_data_presence', auto_ack=True)
            if method_frame:
                message = json.loads(body)
                if message['sensor_type'] == 'presence':
                    value = "ON" if message['value'] == 1 else "OFF"
                    response = smart_home_pb2.ObjectResponse(values=[smart_home_pb2.ObjectValue(type="PRESENCE", value=value)])
                    yield response
            
            method_frame, header_frame, body = channel.basic_get(queue='sensor_data_temperature', auto_ack=True)
            if method_frame:
                message = json.loads(body)
                print(message)
                if message['sensor_type'] == 'temperature':
                    value = f"{message['value']}"
                    print("Sensor Temp:", message)
                    response = smart_home_pb2.ObjectResponse(values=[smart_home_pb2.ObjectValue(type="TEMPERATURE", value=value)])
                    yield response
            
            method_frame, header_frame, body = channel.basic_get(queue='sensor_data_humidity', auto_ack=True)
            if method_frame:
                message = json.loads(body)
                print("Sensor Humidty:", message)
                if message['sensor_type'] == 'humidity':
                    value = f"{message['value']}"
                    response = smart_home_pb2.ObjectResponse(values=[smart_home_pb2.ObjectValue(type="HUMIDITY", value=value)])
                    yield response
                        
        '''if sensor_type == smart_home_pb2.PRESENCE:
            while context.is_active():
                response = []
                
                method_frame, header_frame, body = channel.basic_get(queue='sensor_data_presence', auto_ack=True)
                if method_frame:
                    message = json.loads(body)
                    if message['sensor_type'] == 'presence':
                        value = "ON" if message['value'] == 1 else "OFF"
                        response = smart_home_pb2.ObjectResponse(values=[smart_home_pb2.ObjectValue(type="PRESENCE", value=value)])
                        yield response
                
                method_frame, header_frame, body = channel.basic_get(queue='sensor_data_temperature', auto_ack=True)
                if method_frame:
                    message = json.loads(body)
                    print(message)
                    if message['sensor_type'] == 'temperature':
                        value = f"{message['value']}"
                        print("Sensor Temp:", message)
                        response = smart_home_pb2.ObjectResponse(values=[smart_home_pb2.ObjectValue(type="TEMPERATURE", value=value)])
                        yield response
        elif sensor_type == smart_home_pb2.TEMPERATURE:
            while context.is_active():
                response = []
                
                method_frame, header_frame, body = channel.basic_get(queue='sensor_data_temperature', auto_ack=True)
                if method_frame:
                    message = json.loads(body)
                    print(message)
                    if message['sensor_type'] == 'temperature':
                        value = f"{message['value']}"
                        print("Sensor Temp:", message)
                        response = smart_home_pb2.ObjectResponse(values=[smart_home_pb2.ObjectValue(type="temperature", value=value)])
                        yield response
        elif sensor_type == smart_home_pb2.HUMIDITY:
            while context.is_active():
                response = []
                
                method_frame, header_frame, body = channel.basic_get(queue='sensor_data_humidity', auto_ack=True)
                if method_frame:
                    message = json.loads(body)
                    print("Sensor Humidty:", message)
                    if message['sensor_type'] == 'humidity':
                        value = f"{message['value']}"
                        response = smart_home_pb2.ObjectResponse(values=[smart_home_pb2.ObjectValue(type="humidity", value=value)])
                        yield response
        else:
            response = []
            response.append(smart_home_pb2.ObjectValue(type="error", value="Object does not exist"))
            context.abort(grpc.StatusCode.NOT_FOUND, "Sensor not recognized", smart_home_pb2.ObjectResponse(values=response))

    def GetSensorValues2(self, request, context):
        sensor_type = request.type

        if sensor_type == smart_home_pb2.PRESENCE:
            while context.is_active():
                response = []
                
                method_frame, header_frame, body = channel.basic_get(queue='sensor_data_presence', auto_ack=True)
                if method_frame:
                    message = json.loads(body)
                    if message['sensor_type'] == 'presence':
                        value = "ON" if message['value'] == 1 else "OFF"
                        response = smart_home_pb2.ObjectResponse(values=[smart_home_pb2.ObjectValue(type="status", value=value)])
                        yield response
        elif sensor_type == smart_home_pb2.TEMPERATURE:
            while context.is_active():
                response = []
                
                method_frame, header_frame, body = channel.basic_get(queue='sensor_data_temperature', auto_ack=True)
                if method_frame:
                    message = json.loads(body)
                    print(message)
                    if message['sensor_type'] == 'temperature':
                        value = f"{message['value']}"
                        print("Sensor Temp:", message)
                        response = smart_home_pb2.ObjectResponse(values=[smart_home_pb2.ObjectValue(type="temperature", value=value)])
                        yield response
        elif sensor_type == smart_home_pb2.HUMIDITY:
            while context.is_active():
                response = []
                
                method_frame, header_frame, body = channel.basic_get(queue='sensor_data_humidity', auto_ack=True)
                if method_frame:
                    message = json.loads(body)
                    print("Sensor Humidty:", message)
                    if message['sensor_type'] == 'humidity':
                        value = f"{message['value']}"
                        response = smart_home_pb2.ObjectResponse(values=[smart_home_pb2.ObjectValue(type="humidity", value=value)])
                        yield response
        else:
            response = []
            response.append(smart_home_pb2.ObjectValue(type="error", value="Object does not exist"))
            context.abort(grpc.StatusCode.NOT_FOUND, "Sensor not recognized", smart_home_pb2.ObjectResponse(values=response))'''

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    smart_home_pb2_grpc.add_ClientServiceServicer_to_server(ClientService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
