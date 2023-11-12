from concurrent import futures
import grpc
import smart_home_pb2
import smart_home_pb2_grpc
import time

# Variável global para manter a temperatura desejada
desired_temperature = 27.0  # Exemplo inicial
lamp_state = False

class LampService(smart_home_pb2_grpc.LampServiceServicer):
    def SetState(self, request, context):
        global lamp_state
        lamp_state = request.state
        print(f"The value of the lamp is set to {lamp_state}")
        return smart_home_pb2.LampResponse(success=True)

class ThermostatService(smart_home_pb2_grpc.ThermostatServiceServicer):

    def UpdateDesiredTemperature(self, request, context):
        global desired_temperature
        desired_temperature = request.temperature
        print(f"Updated desired temperature to {desired_temperature}°C")
        return smart_home_pb2.TemperatureResponse(success=True)

    def SetTemperature(self, request, context):
        global desired_temperature
        current_temperature = request.temperature
        adjustment = desired_temperature - current_temperature
        if adjustment > 0:
            new_temperature = desired_temperature + adjustment
            print(f"Current temperature is {current_temperature}°C, adjusting to {new_temperature}°C")
            # A lógica de controle do termostato seria implementada aqui
        else:
            print(f"Current temperature is {current_temperature}°C, no adjustment needed.")
        return smart_home_pb2.TemperatureResponse(success=True)

class ClientService(smart_home_pb2_grpc.ClientServiceServicer):
    def SetActuatorValues(self, request, context):
        actuator_type = request.type
        value = request.value
        response = []

        if actuator_type == smart_home_pb2.LAMP:
            print("Setting lamp value:", value)
            response.append(smart_home_pb2.ObjectValue(type="status", value="ON"))
            # Lógica para mudar valor da lâmpada
        elif actuator_type == smart_home_pb2.THERMOSTAT:
            print("Setting thermostat value:", value)
            response.append(smart_home_pb2.ObjectValue(type="temperature", value=value))
            # Lógica para mudar valor do termostato
        elif actuator_type == smart_home_pb2.IRRIGATOR:
            print("Setting irrigator value:", value)
            response.append(smart_home_pb2.ObjectValue(type="status", value="OFF"))
            # Lógica para mudar valor da irrigador
        else:
            response.append(smart_home_pb2.ObjectValue(type="error", value="Objeto não existe"))

        return smart_home_pb2.ObjectResponse(values=response)
    
    def GetActuatorValues(self, request, context):
        actuator_type = request.type
        response = []

        if actuator_type == smart_home_pb2.LAMP:
            response.append(smart_home_pb2.ObjectValue(type="status", value="ON"))
        elif actuator_type == smart_home_pb2.THERMOSTAT:
            response.append(smart_home_pb2.ObjectValue(type="temperature", value="25"))
        elif actuator_type == smart_home_pb2.IRRIGATOR:
            response.append(smart_home_pb2.ObjectValue(type="status",  value="OFF"))
        else:
            response.append(smart_home_pb2.ObjectValue(type="error", value="Objeto não existe"))
        
        return smart_home_pb2.ObjectResponse(values=response)

    def GetSensorValues(self, request, context):
        sensor_type = request.type

        if sensor_type == smart_home_pb2.PRESENCE:
            while context.is_active():
                response = []
                # Simulação contínua de leituras de presença
                value = str(int(time.time()) % 2)  # Simulação de valores (0 ou 1)
                if value == 0: value = "ON"
                else: value = "OFF"
                
                response.append(smart_home_pb2.ObjectValue(type="status", value=value))
                yield smart_home_pb2.ObjectResponse(values=response)
                time.sleep(10)

        elif sensor_type == smart_home_pb2.TEMPERATURE:
            while context.is_active():
                response = []
                # Simulação contínua de leituras de temperatura
                value = str(20 + int(time.time()))  # Simulação de valores variáveis
                value = f"{value}"
                
                response.append(smart_home_pb2.ObjectValue(type="temperature", value=value))
                yield smart_home_pb2.ObjectResponse(values=response)
                time.sleep(10)

        elif sensor_type == smart_home_pb2.HUMIDITY:
            while context.is_active():
                response = []
                # Simulação contínua de leituras de umidade
                value = str(50 + int(time.time()))  # Simulação de valores variáveis
                value = f"{value}"
                
                response.append(smart_home_pb2.ObjectValue(type="humity", value=value))
                yield smart_home_pb2.ObjectResponse(values=response)
                time.sleep(10)
        else:
            response = []
            response.append(smart_home_pb2.ObjectValue(type="error", value="Object does not exist"))
            context.abort(grpc.StatusCode.NOT_FOUND, "Sensor not recognized", smart_home_pb2.ObjectResponse(values=response))
            

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    smart_home_pb2_grpc.add_ThermostatServiceServicer_to_server(ThermostatService(), server)
    smart_home_pb2_grpc.add_ClientServiceServicer_to_server(ClientService(), server)
    smart_home_pb2_grpc.add_LampServiceServicer_to_server(LampService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Smart Home Server running...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
