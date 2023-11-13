# smart_home_parte_2
Link para aplicação cliente: [Cliente JavaScript](https://github.com/Maurrici/smart-home-grpc/tree/master)
### Gerando arquivos protocol buffers e grpc
```
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./smart_home.proto
```

Este projeto simula um ambiente de casa inteligente, integrando sensores e atuadores através de RabbitMQ e gRPC, utilizando Python.

## Funcionalidades

- **Sensores**: Simulação de sensores de temperatura, umidade e presença, que publicam leituras periodicamente para filas específicas no RabbitMQ.
- **Atuadores**: Implementação de atuadores como lâmpada, termostato e irrigador, controlados via gRPC.
- **Home Assistant**: Um serviço que consome mensagens RabbitMQ dos sensores e interage com atuadores via gRPC.
- **Servidor gRPC**: Um servidor que expõe serviços para controlar os atuadores e responder a requisições de atualização.
- **Comunicação**: Utilização de RabbitMQ para comunicação assíncrona entre sensores e o Home Assistant, e gRPC para comandos dos atuadores.
- **Cliente JavaScript**: Uma interface de usuário web para interagir com os atuadores e visualizar dados dos sensores.

## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:
- Python 3.x
- RabbitMQ
- Node.js
- Bibliotecas Python: `pika`, `grpcio`, `grpcio-tools`
- Dependências Node.js (consulte `package.json` no repositório do cliente)

## Configuração do Ambiente

1. Instale as dependências do Python utilizando pip:

```sh
pip install pika grpcio grpcio-tools
