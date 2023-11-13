from concurrent import futures
import grpc
import smart_home_pb2
import smart_home_pb2_grpc
import time
import random

# Variável global
desired_temperature = 27.0

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



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    smart_home_pb2_grpc.add_ThermostatServiceServicer_to_server(ThermostatService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Thermostate running...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

