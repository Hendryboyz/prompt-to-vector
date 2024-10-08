# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import embedded_encode_pb2 as embedded__encode__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in embedded_encode_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class EmbeddedEncodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EncodeSentence = channel.unary_unary(
                '/EmbeddedEncode/EncodeSentence',
                request_serializer=embedded__encode__pb2.EncodingRequest.SerializeToString,
                response_deserializer=embedded__encode__pb2.EncodedVectors.FromString,
                _registered_method=True)
        self.Hello = channel.unary_unary(
                '/EmbeddedEncode/Hello',
                request_serializer=embedded__encode__pb2.HelloRequest.SerializeToString,
                response_deserializer=embedded__encode__pb2.HelloReply.FromString,
                _registered_method=True)


class EmbeddedEncodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EncodeSentence(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Hello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmbeddedEncodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EncodeSentence': grpc.unary_unary_rpc_method_handler(
                    servicer.EncodeSentence,
                    request_deserializer=embedded__encode__pb2.EncodingRequest.FromString,
                    response_serializer=embedded__encode__pb2.EncodedVectors.SerializeToString,
            ),
            'Hello': grpc.unary_unary_rpc_method_handler(
                    servicer.Hello,
                    request_deserializer=embedded__encode__pb2.HelloRequest.FromString,
                    response_serializer=embedded__encode__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EmbeddedEncode', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('EmbeddedEncode', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EmbeddedEncode(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EncodeSentence(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/EmbeddedEncode/EncodeSentence',
            embedded__encode__pb2.EncodingRequest.SerializeToString,
            embedded__encode__pb2.EncodedVectors.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Hello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/EmbeddedEncode/Hello',
            embedded__encode__pb2.HelloRequest.SerializeToString,
            embedded__encode__pb2.HelloReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
