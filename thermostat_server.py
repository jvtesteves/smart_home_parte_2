from concurrent import futures
import grpc
import thermostat_pb2
import thermostat_pb2_grpc
import time

# Variável global para manter a temperatura desejada
desired_temperature = 27.0  # Exemplo inicial

class ThermostatService(thermostat_pb2_grpc.ThermostatServiceServicer):

    def UpdateDesiredTemperature(self, request, context):
        global desired_temperature
        desired_temperature = request.temperature
        print(f"Updated desired temperature to {desired_temperature}°C")
        return thermostat_pb2.TemperatureResponse(success=True)

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
        return thermostat_pb2.TemperatureResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    thermostat_pb2_grpc.add_ThermostatServiceServicer_to_server(ThermostatService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Thermostat Server running...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
