import asyncio

import logging

import grpc
import embedded_encode_pb2_grpc
import embedded_encode_pb2


async def run() -> None:
    print("Will try to encode sentence to vector ...")
    async with grpc.aio.insecure_channel("localhost:30052") as channel:
        stub = embedded_encode_pb2_grpc.EmbeddedEncodeStub(channel)
        sentences = [
            "The weather is lovely today.",
            "It's so sunny outside!",
            "He drove to the stadium.",
        ]
        response = await stub.Hello(embedded_encode_pb2.HelloRequest(message="world"))
        print(f'Encode client received: {response.message}')
        response = await stub.EncodeSentence(embedded_encode_pb2.EncodingRequest(sentences=sentences))
        
        vectors = [ v.vector for v in response.vectors ]
        print(f'Encode client received: {vectors}')


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
