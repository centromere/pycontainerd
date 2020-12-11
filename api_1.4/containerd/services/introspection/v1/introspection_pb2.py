# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/services/introspection/v1/introspection.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.types import platform_pb2 as containerd_dot_types_dot_platform__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from containerd.gogoproto import gogo_pb2 as containerd_dot_gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/services/introspection/v1/introspection.proto',
  package='containerd.services.introspection.v1',
  syntax='proto3',
  serialized_options=b'ZLgithub.com/containerd/containerd/api/services/introspection/v1;introspection',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8containerd/services/introspection/v1/introspection.proto\x12$containerd.services.introspection.v1\x1a\x1f\x63ontainerd/types/platform.proto\x1a\x17google/rpc/status.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1f\x63ontainerd/gogoproto/gogo.proto\"\xa1\x02\n\x06Plugin\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08requires\x18\x03 \x03(\t\x12\x33\n\tplatforms\x18\x04 \x03(\x0b\x32\x1a.containerd.types.PlatformB\x04\xc8\xde\x1f\x00\x12J\n\x07\x65xports\x18\x05 \x03(\x0b\x32\x39.containerd.services.introspection.v1.Plugin.ExportsEntry\x12\x14\n\x0c\x63\x61pabilities\x18\x06 \x03(\t\x12$\n\x08init_err\x18\x07 \x01(\x0b\x32\x12.google.rpc.Status\x1a.\n\x0c\x45xportsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"!\n\x0ePluginsRequest\x12\x0f\n\x07\x66ilters\x18\x01 \x03(\t\"V\n\x0fPluginsResponse\x12\x43\n\x07plugins\x18\x01 \x03(\x0b\x32,.containerd.services.introspection.v1.PluginB\x04\xc8\xde\x1f\x00\"(\n\x0eServerResponse\x12\x16\n\x04uuid\x18\x01 \x01(\tB\x08\xe2\xde\x1f\x04UUID2\xdf\x01\n\rIntrospection\x12v\n\x07Plugins\x12\x34.containerd.services.introspection.v1.PluginsRequest\x1a\x35.containerd.services.introspection.v1.PluginsResponse\x12V\n\x06Server\x12\x16.google.protobuf.Empty\x1a\x34.containerd.services.introspection.v1.ServerResponseBNZLgithub.com/containerd/containerd/api/services/introspection/v1;introspectionX\x03\x62\x06proto3'
  ,
  dependencies=[containerd_dot_types_dot_platform__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,containerd_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PLUGIN_EXPORTSENTRY = _descriptor.Descriptor(
  name='ExportsEntry',
  full_name='containerd.services.introspection.v1.Plugin.ExportsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.services.introspection.v1.Plugin.ExportsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.services.introspection.v1.Plugin.ExportsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=462,
  serialized_end=508,
)

_PLUGIN = _descriptor.Descriptor(
  name='Plugin',
  full_name='containerd.services.introspection.v1.Plugin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='containerd.services.introspection.v1.Plugin.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.services.introspection.v1.Plugin.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requires', full_name='containerd.services.introspection.v1.Plugin.requires', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='platforms', full_name='containerd.services.introspection.v1.Plugin.platforms', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exports', full_name='containerd.services.introspection.v1.Plugin.exports', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='capabilities', full_name='containerd.services.introspection.v1.Plugin.capabilities', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='init_err', full_name='containerd.services.introspection.v1.Plugin.init_err', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PLUGIN_EXPORTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=508,
)


_PLUGINSREQUEST = _descriptor.Descriptor(
  name='PluginsRequest',
  full_name='containerd.services.introspection.v1.PluginsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filters', full_name='containerd.services.introspection.v1.PluginsRequest.filters', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=510,
  serialized_end=543,
)


_PLUGINSRESPONSE = _descriptor.Descriptor(
  name='PluginsResponse',
  full_name='containerd.services.introspection.v1.PluginsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='plugins', full_name='containerd.services.introspection.v1.PluginsResponse.plugins', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=545,
  serialized_end=631,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='containerd.services.introspection.v1.ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='containerd.services.introspection.v1.ServerResponse.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\004UUID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=633,
  serialized_end=673,
)

_PLUGIN_EXPORTSENTRY.containing_type = _PLUGIN
_PLUGIN.fields_by_name['platforms'].message_type = containerd_dot_types_dot_platform__pb2._PLATFORM
_PLUGIN.fields_by_name['exports'].message_type = _PLUGIN_EXPORTSENTRY
_PLUGIN.fields_by_name['init_err'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_PLUGINSRESPONSE.fields_by_name['plugins'].message_type = _PLUGIN
DESCRIPTOR.message_types_by_name['Plugin'] = _PLUGIN
DESCRIPTOR.message_types_by_name['PluginsRequest'] = _PLUGINSREQUEST
DESCRIPTOR.message_types_by_name['PluginsResponse'] = _PLUGINSRESPONSE
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Plugin = _reflection.GeneratedProtocolMessageType('Plugin', (_message.Message,), {

  'ExportsEntry' : _reflection.GeneratedProtocolMessageType('ExportsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLUGIN_EXPORTSENTRY,
    '__module__' : 'containerd.services.introspection.v1.introspection_pb2'
    # @@protoc_insertion_point(class_scope:containerd.services.introspection.v1.Plugin.ExportsEntry)
    })
  ,
  'DESCRIPTOR' : _PLUGIN,
  '__module__' : 'containerd.services.introspection.v1.introspection_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.introspection.v1.Plugin)
  })
_sym_db.RegisterMessage(Plugin)
_sym_db.RegisterMessage(Plugin.ExportsEntry)

PluginsRequest = _reflection.GeneratedProtocolMessageType('PluginsRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINSREQUEST,
  '__module__' : 'containerd.services.introspection.v1.introspection_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.introspection.v1.PluginsRequest)
  })
_sym_db.RegisterMessage(PluginsRequest)

PluginsResponse = _reflection.GeneratedProtocolMessageType('PluginsResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINSRESPONSE,
  '__module__' : 'containerd.services.introspection.v1.introspection_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.introspection.v1.PluginsResponse)
  })
_sym_db.RegisterMessage(PluginsResponse)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRESPONSE,
  '__module__' : 'containerd.services.introspection.v1.introspection_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.introspection.v1.ServerResponse)
  })
_sym_db.RegisterMessage(ServerResponse)


DESCRIPTOR._options = None
_PLUGIN_EXPORTSENTRY._options = None
_PLUGIN.fields_by_name['platforms']._options = None
_PLUGINSRESPONSE.fields_by_name['plugins']._options = None
_SERVERRESPONSE.fields_by_name['uuid']._options = None

_INTROSPECTION = _descriptor.ServiceDescriptor(
  name='Introspection',
  full_name='containerd.services.introspection.v1.Introspection',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=676,
  serialized_end=899,
  methods=[
  _descriptor.MethodDescriptor(
    name='Plugins',
    full_name='containerd.services.introspection.v1.Introspection.Plugins',
    index=0,
    containing_service=None,
    input_type=_PLUGINSREQUEST,
    output_type=_PLUGINSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Server',
    full_name='containerd.services.introspection.v1.Introspection.Server',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_INTROSPECTION)

DESCRIPTOR.services_by_name['Introspection'] = _INTROSPECTION

# @@protoc_insertion_point(module_scope)
