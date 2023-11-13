import pika
import json
import time
from random import uniform

# Configurações do RabbitMQ
rabbitmq_host = 'localhost'
queue_name = 'sensor_data'
humidity_queue_name = 'sensor_data_humidity'  # Nova fila para umidade

# Estabelece conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Declara as filas onde as mensagens serão publicadas
channel.queue_declare(queue=queue_name)
channel.queue_declare(queue=humidity_queue_name)  # Declaração da nova fila


def publish_sensor_data():
    while True:
        # Simula a leitura do sensor de umidade
        humidity = round(uniform(20.0, 90.0), 0)
        message = json.dumps({'sensor_type': 'humidity', 'value': humidity})

        # Publica a mensagem nas filas
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=message)
        channel.basic_publish(exchange='',
                              routing_key=humidity_queue_name,
                              body=message)
        print(f"[x] Sent {message}")
        time.sleep(10)  # Intervalo entre as publicações


publish_sensor_data()
