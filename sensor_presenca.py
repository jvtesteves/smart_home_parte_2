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

def publish_sensor_presence():
    while True:
        # Simula a leitura do sensor de temperatura
        presence = round(uniform(0, 1), 0)
        message = json.dumps({'sensor_type': 'presence', 'value': presence})

        # Publica a mensagem na fila
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=message)
        print(f"[x] Sent {message}")
        time.sleep(60)  # Intervalo entre as publicações

publish_sensor_presence()

