# smart_home_parte_2

### Gerando arquivos protocol buffers e grpc
```
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./smart_home.proto
```
