from concurrent import futures
import grpc
import smart_home_pb2
import smart_home_pb2_grpc
import time
import random

# Variável global
desired_humidity = 60
irrigator_state = False

class IrrigatorService(smart_home_pb2_grpc.IrrigatorServiceServicer):

    def SetStateIrrigator(self, request, context):
        global desired_humidity
        current_humidity = request.state
        global irrigator_state
        irrigator_state = request.state
        if (current_humidity >= desired_humidity):
            print(f"Current humidity is {current_humidity}%. The value of the irrigator is set to {irrigator_state}")
        else:
            print(f"Current humidity is {current_humidity}%. The value of the irrigator is set to {irrigator_state}")
        return smart_home_pb2.IrrigatorResponse(success=True)

    def GetStateIrrigator(self, request, context):
        global irrigator_state
        return smart_home_pb2.IrrigatorResponse(success=irrigator_state)

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
