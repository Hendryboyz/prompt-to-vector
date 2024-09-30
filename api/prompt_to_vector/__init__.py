import grpc
import logging
from prompt_to_vector import embedded_encode_pb2
from prompt_to_vector import embedded_encode_pb2_grpc
from prompt_to_vector.inference import TextEncoder

class Encoder(embedded_encode_pb2_grpc.EmbeddedEncodeServicer):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Encoder, cls).__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        super().__init__()
        self.text_encoder = TextEncoder()
        self.logger = logging.getLogger('encoder')
    
    async def EncodeSentence(
        self,
        request: embedded_encode_pb2.EncodingRequest,
        context: grpc.aio.ServicerContext,
    ) -> embedded_encode_pb2.EncodedVectors:
        logging.debug(request.sentences)
        vectors = self.text_encoder.encode_sentences(request.sentences)
        
        return embedded_encode_pb2.EncodedVectors(
            vectors=[ embedded_encode_pb2.Vector(vector=v) for v in vectors.tolist() ]
        )
    
    async def Hello(
        self,
        request: embedded_encode_pb2.HelloRequest,
        context: grpc.aio.ServicerContext,
    ) -> embedded_encode_pb2.HelloReply:
        print(request.message)
        return embedded_encode_pb2.HelloReply(message=f'Hello, {request.message}')
    
    
def add_server(grpc_server: grpc.Server) -> None:
    embedded_encode_pb2_grpc.add_EmbeddedEncodeServicer_to_server(Encoder(), grpc_server)
    
