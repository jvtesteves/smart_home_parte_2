import pika
import json
import time
from random import uniform

# Configurações do RabbitMQ
rabbitmq_host = 'localhost'  # ou o IP/host onde seu RabbitMQ está rodando
queue_name = 'sensor_data'

# Estabelece conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Declara a fila onde as mensagens serão publicadas
channel.queue_declare(queue=queue_name)


def publish_sensor_data():
    while True:
        # Simula a leitura do sensor de temperatura
        temperature = round(uniform(18.0, 26.0), 2)
        message = json.dumps({'sensor_type': 'temperature', 'value': temperature})

        # Publica a mensagem na fila
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=message)
        print(f"[x] Sent {message}")
        time.sleep(15)  # Intervalo entre as publicações


publish_sensor_data()
