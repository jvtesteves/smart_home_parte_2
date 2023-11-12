import pika
import json
import grpc
import smart_home_pb2
import smart_home_pb2_grpc

# Configurações do RabbitMQ
rabbitmq_host = 'localhost'
queue_name = 'sensor_data'

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Declarar a fila para consumo
channel.queue_declare(queue=queue_name)

# Temperatura desejada (definida pelo "usuário")
user_set_temperature = 27.0

# Função para chamar o serviço gRPC do termostato
def set_temperature(current_temperature):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = smart_home_pb2_grpc.ThermostatServiceStub(channel)
        # Aqui o Home Assistant envia a temperatura atual do sensor para o termostato
        response = stub.SetTemperature(smart_home_pb2.TemperatureRequest(temperature=current_temperature))
        print(f"Thermostat response: {response.success}")

# Função para atualizar a temperatura desejada no termostato
def update_desired_temperature(desired_temp):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = smart_home_pb2_grpc.ThermostatServiceStub(channel)
        response = stub.UpdateDesiredTemperature(smart_home_pb2.TemperatureRequest(temperature=desired_temp))
        print(f"Updated desired temperature to {desired_temp}°C: {response.success}")


def set_humidity(current_humidity):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = smart_home_pb2_grpc.IrrigatorServiceStub(channel)
        # Aqui o Home Assistant envia a temperatura atual do sensor para o termostato
        response = stub.SetHumidity(smart_home_pb2.HumidityRequest(humidity=current_humidity))
        print(f"Irrigator response: {response.success}")

def update_desired_humidity(desired_humidity):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = smart_home_pb2_grpc.IrrigatorServiceStub(channel)
        response = stub.UpdateDesiredHumidity(smart_home_pb2.HumidityRequest(humidity=desired_humidity))
        print(f"Updated desired temperature to {desired_humidity}°C: {response.success}")


def set_presence(presence):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = smart_home_pb2_grpc.LampServiceStub(channel)
        state = True if presence == 1 else False
        response = stub.SetState(smart_home_pb2.LampRequest(state=state))
        print(f"Updated lamp state to {state}: {response.success}")


# Função de callback para quando uma mensagem é recebida da fila do RabbitMQ
def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"[x] Received {message}")
    if message['sensor_type'] == 'temperature':
        # Ajusta a temperatura do termostato com base na leitura do sensor
        set_temperature(message['value'])
    elif message['sensor_type'] == 'presence':
        set_presence(message['value'])
    elif message['sensor_type'] == 'humidity':
        set_humidity(message['value'])

# Configurar a função de callback no canal do RabbitMQ
channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

# Iniciar o consumo de mensagens
channel.start_consuming()
