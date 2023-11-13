import pika
import json
import time
from random import randint

# Configurações do RabbitMQ
rabbitmq_host = 'localhost'
queue_name = 'sensor_data'
presence_queue_name = 'sensor_data_presence'  # Nova fila para presença

# Estabelece conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Declara as filas onde as mensagens serão publicadas
channel.queue_declare(queue=queue_name)
channel.queue_declare(queue=presence_queue_name)  # Declaração da nova fila

last_state = None


def publish_sensor_data():
    global last_state
    while True:
        # Simula a detecção de presença (0 ou 1)
        presence = randint(0, 1)
        if presence != last_state:
            last_state = presence
            message = json.dumps({'sensor_type': 'presence', 'value': presence})

            # Publica a mensagem nas filas
            channel.basic_publish(exchange='',
                                  routing_key=queue_name,
                                  body=message)
            channel.basic_publish(exchange='',
                                  routing_key=presence_queue_name,
                                  body=message)
            print(f"[x] Sent {message}")
        time.sleep(5)  # Intervalo entre as publicações


publish_sensor_data()
