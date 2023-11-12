from concurrent import futures
import grpc
import smart_home_pb2
import smart_home_pb2_grpc
import time
import random

# Variável global
desired_humidity = 60


class IrrigatorService(smart_home_pb2_grpc.IrrigatorServiceServicer):

    def UpdateDesiredHumidity(self, request, context):
        global desired_humidity
        desired_humidity = request.humidity
        print(f"Updated desired humidity to {desired_humidity}%")
        return smart_home_pb2.HumidityResponse(success=True)

    def SetHumidity(self, request, context):
        global desired_humidity
        current_humidity = request.humidity
        humidity_threshold = 8 # 8% de umidade acima e abaixo do valor desejado é aceitável
        if abs(desired_humidity - current_humidity > humidity_threshold):
            if(current_humidity > desired_humidity + humidity_threshold):
                print(f"Current humidity is {current_humidity}%, turning OFF irrigator...")
            else:
                print(f"Current humidity is {current_humidity}%, turning ON irrigator...")
        else:
            print(f"Current humidity is {current_humidity}%, no adjustment needed.")
        return smart_home_pb2.HumidityResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    smart_home_pb2_grpc.add_IrrigatorServiceServicer_to_server(IrrigatorService(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    print("Irrigator running...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
