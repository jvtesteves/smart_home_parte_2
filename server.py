from concurrent import futures
import grpc
import smart_home_pb2
import smart_home_pb2_grpc
import time
import random

class ClientService(smart_home_pb2_grpc.ClientServiceServicer):
    def SetActuatorValues(self, request, context):
        actuator_type = request.type
        value = request.value
        response = []

        if actuator_type == smart_home_pb2.LAMP:
            print("Setting lamp value:", value)
            response.append(smart_home_pb2.ObjectValue(type="status", value=value))
            # Lógica para mudar valor da lâmpada
        elif actuator_type == smart_home_pb2.THERMOSTAT:
            print("Setting thermostat value:", value)
            response.append(smart_home_pb2.ObjectValue(type="temperature", value=value))
            # Lógica para mudar valor do termostato
        elif actuator_type == smart_home_pb2.IRRIGATOR:
            print("Setting irrigator value:", value)
            response.append(smart_home_pb2.ObjectValue(type="status", value=value))
            # Lógica para mudar valor da irrigador
        else:
            response.append(smart_home_pb2.ObjectValue(type="error", value="Objeto não existe"))

        return smart_home_pb2.ObjectResponse(values=response)
    
    def GetActuatorValues(self, request, context):
        actuator_type = request.type
        response = []

        if actuator_type == smart_home_pb2.LAMP:
            random_value = random.randint(0, 1)
            value = "ON"
            if random_value == 0: value = "OFF"
            response.append(smart_home_pb2.ObjectValue(type="status", value=value))
        elif actuator_type == smart_home_pb2.THERMOSTAT:
            random_value = random.randrange(10, 30)
            response.append(smart_home_pb2.ObjectValue(type="temperature", value=f"{random_value}"))
        elif actuator_type == smart_home_pb2.IRRIGATOR:
            random_value = random.randint(0, 1)
            value = "ON"
            if random_value == 0: value = "OFF"
            response.append(smart_home_pb2.ObjectValue(type="status",  value=value))
        else:
            response.append(smart_home_pb2.ObjectValue(type="error", value="Objeto não existe"))
        
        return smart_home_pb2.ObjectResponse(values=response)

    def GetSensorValues(self, request, context):
        sensor_type = request.type

        if sensor_type == smart_home_pb2.PRESENCE:
            while context.is_active():
                response = []
                # Simulação contínua de leituras de presença
                random_value = random.randint(0, 1)
                value = "ON"
                if random_value == 0: value = "OFF"
                
                response.append(smart_home_pb2.ObjectValue(type="status", value=value))
                yield smart_home_pb2.ObjectResponse(values=response)
                time.sleep(5)

        elif sensor_type == smart_home_pb2.TEMPERATURE:
            while context.is_active():
                response = []
                # Simulação contínua de leituras de temperatura
                value = str(random.randrange(10, 30))  # Simulação de valores variáveis
                value = f"{value}"
                
                response.append(smart_home_pb2.ObjectValue(type="temperature", value=value))
                yield smart_home_pb2.ObjectResponse(values=response)
                time.sleep(5)

        elif sensor_type == smart_home_pb2.HUMIDITY:
            while context.is_active():
                response = []
                # Simulação contínua de leituras de umidade
                value = str(random.randrange(10, 30))  # Simulação de valores variáveis
                value = f"{value}"
                
                response.append(smart_home_pb2.ObjectValue(type="humity", value=value))
                yield smart_home_pb2.ObjectResponse(values=response)
                time.sleep(5)
        else:
            response = []
            response.append(smart_home_pb2.ObjectValue(type="error", value="Object does not exist"))
            context.abort(grpc.StatusCode.NOT_FOUND, "Sensor not recognized", smart_home_pb2.ObjectResponse(values=response))
            
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
