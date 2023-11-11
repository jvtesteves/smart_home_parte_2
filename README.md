# smart_home_parte_2
Link para aplicação cliente: [Cliente JavaScript](https://github.com/Maurrici/smart-home-grpc/tree/master)
### Gerando arquivos protocol buffers e grpc
```
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./smart_home.proto
```

Este projeto simula um ambiente de casa inteligente, integrando sensores e atuadores através de RabbitMQ e gRPC, utilizando Python.

## Funcionalidades Iniciais

- **Sensores**: Simulação de sensores de temperatura que publicam leituras periodicamente para uma fila RabbitMQ.
- **Home Assistant**: Um consumidor de mensagens RabbitMQ que processa leituras de sensores e toma decisões de controle.
- **Servidor gRPC**: Um servidor que expõe serviços para controlar um termostato virtual e responder a requisições de atualização de temperatura.
- **Comunicação**: Utilização de RabbitMQ para comunicação assíncrona entre sensores e o Home Assistant, e gRPC para comandos de atuadores.

## Pré-requisitos

Antes de iniciar, certifique-se de que você tem o Python 3.x instalado, juntamente com o RabbitMQ e as seguintes bibliotecas Python:
- `pika`
- `grpcio`
- `grpcio-tools`

## Configuração do Ambiente

1. Instale as dependências do Python utilizando pip:

```sh
pip install pika grpcio grpcio-tools
