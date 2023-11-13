import pika
import json
import time
from random import uniform

# Configurações do RabbitMQ
rabbitmq_host = 'localhost'
queue_name = 'sensor_data'
temperature_queue_name = 'sensor_data_temperature'  # Nova fila para temperatura

# Estabelece conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Declara as filas onde as mensagens serão publicadas
channel.queue_declare(queue=queue_name)
channel.queue_declare(queue=temperature_queue_name)  # Declaração da nova fila


def publish_sensor_data():
    while True:
        # Simula a leitura do sensor de temperatura
        temperature = round(uniform(18.0, 26.0), 0)
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
