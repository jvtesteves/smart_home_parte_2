from concurrent import futures
import grpc
import smart_home_pb2
import smart_home_pb2_grpc
import time
import random

# Variável global
lamp_state = False

class LampService(smart_home_pb2_grpc.LampServiceServicer):
    def SetState(self, request, context):
        global lamp_state
        lamp_state = request.state
        print(f"The value of the lamp is set to {lamp_state}")
        return smart_home_pb2.LampResponse(success=True)
    
    def GetState(self, request, context):
        global lamp_state
        return smart_home_pb2.IrrigatorResponse(state=lamp_state, success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    smart_home_pb2_grpc.add_LampServiceServicer_to_server(LampService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Lamp running...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()