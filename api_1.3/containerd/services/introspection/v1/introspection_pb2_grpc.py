# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from containerd.services.introspection.v1 import introspection_pb2 as containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class IntrospectionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Plugins = channel.unary_unary(
                '/containerd.services.introspection.v1.Introspection/Plugins',
                request_serializer=containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.PluginsRequest.SerializeToString,
                response_deserializer=containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.PluginsResponse.FromString,
                )
        self.Server = channel.unary_unary(
                '/containerd.services.introspection.v1.Introspection/Server',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.ServerResponse.FromString,
                )


class IntrospectionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Plugins(self, request, context):
        """Plugins returns a list of plugins in containerd.

        Clients can use this to detect features and capabilities when using
        containerd.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Server(self, request, context):
        """Server returns information about the containerd server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IntrospectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Plugins': grpc.unary_unary_rpc_method_handler(
                    servicer.Plugins,
                    request_deserializer=containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.PluginsRequest.FromString,
                    response_serializer=containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.PluginsResponse.SerializeToString,
            ),
            'Server': grpc.unary_unary_rpc_method_handler(
                    servicer.Server,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.ServerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'containerd.services.introspection.v1.Introspection', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Introspection(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Plugins(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.introspection.v1.Introspection/Plugins',
            containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.PluginsRequest.SerializeToString,
            containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.PluginsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Server(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.introspection.v1.Introspection/Server',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            containerd_dot_services_dot_introspection_dot_v1_dot_introspection__pb2.ServerResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
