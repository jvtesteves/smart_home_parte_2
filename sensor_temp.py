import pika
import json
import time
import grpc
from random import uniform
import smart_home_pb2
import smart_home_pb2_grpc

# Configurações do RabbitMQ
rabbitmq_host = 'localhost'
queue_name = 'sensor_data'
temperature_queue_name = 'sensor_data_temperature'

# Estabelece conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Declara as filas onde as mensagens serão publicadas
channel.queue_declare(queue=queue_name)
channel.queue_declare(queue=temperature_queue_name)


def get_desired_temperature():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = smart_home_pb2_grpc.ThermostatServiceStub(channel)
        response = stub.GetTemperature(smart_home_pb2.Empty())
        return response.temperature


def publish_sensor_data():
    while True:
        # Obtem a temperatura desejada do termostato
        desired_temperature = get_desired_temperature()

        # Gera uma leitura de temperatura dentro de um intervalo de 3 graus da desejada
        temperature = round(uniform(desired_temperature - 1.5, desired_temperature + 1.5), 0)
        message = json.dumps({'sensor_type': 'temperature', 'value': temperature})

        # Publica a mensagem nas filas
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=message)
        channel.basic_publish(exchange='',
                              routing_key=temperature_queue_name,
                              body=message)
        print(f"[x] Sent {message}")
        time.sleep(20)  # Intervalo entre as publicações


publish_sensor_data()
