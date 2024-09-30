#!/bin/bash

python -m grpc_tools.protoc --proto_path=protos \
  --python_out=api/prompt_to_vector \
  --pyi_out=api/prompt_to_vector \
  --grpc_python_out=api/prompt_to_vector \
  protos/embedded_encode.proto

cp -f api/prompt_to_vector/*_pb2* test/