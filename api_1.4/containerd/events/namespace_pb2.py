# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/events/namespace.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.vendor.gogoproto import gogo_pb2 as containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2
from containerd.protobuf.plugin import fieldpath_pb2 as containerd_dot_protobuf_dot_plugin_dot_fieldpath__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/events/namespace.proto',
  package='containerd.events',
  syntax='proto3',
  serialized_options=b'Z2github.com/containerd/containerd/api/events;events\240\364\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!containerd/events/namespace.proto\x12\x11\x63ontainerd.events\x1a&containerd/vendor/gogoproto/gogo.proto\x1a*containerd/protobuf/plugin/fieldpath.proto\"\x8e\x01\n\x0fNamespaceCreate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x06labels\x18\x02 \x03(\x0b\x32..containerd.events.NamespaceCreate.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8e\x01\n\x0fNamespaceUpdate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x06labels\x18\x02 \x03(\x0b\x32..containerd.events.NamespaceUpdate.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1f\n\x0fNamespaceDelete\x12\x0c\n\x04name\x18\x01 \x01(\tB8Z2github.com/containerd/containerd/api/events;events\xa0\xf4\x1e\x01X\x00X\x01\x62\x06proto3'
  ,
  dependencies=[containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,containerd_dot_protobuf_dot_plugin_dot_fieldpath__pb2.DESCRIPTOR,])




_NAMESPACECREATE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='containerd.events.NamespaceCreate.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.events.NamespaceCreate.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.events.NamespaceCreate.LabelsEntry.value', index=1,
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
  serialized_start=238,
  serialized_end=283,
)

_NAMESPACECREATE = _descriptor.Descriptor(
  name='NamespaceCreate',
  full_name='containerd.events.NamespaceCreate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containerd.events.NamespaceCreate.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='containerd.events.NamespaceCreate.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NAMESPACECREATE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=283,
)


_NAMESPACEUPDATE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='containerd.events.NamespaceUpdate.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.events.NamespaceUpdate.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.events.NamespaceUpdate.LabelsEntry.value', index=1,
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
  serialized_start=238,
  serialized_end=283,
)

_NAMESPACEUPDATE = _descriptor.Descriptor(
  name='NamespaceUpdate',
  full_name='containerd.events.NamespaceUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containerd.events.NamespaceUpdate.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='containerd.events.NamespaceUpdate.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NAMESPACEUPDATE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=428,
)


_NAMESPACEDELETE = _descriptor.Descriptor(
  name='NamespaceDelete',
  full_name='containerd.events.NamespaceDelete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containerd.events.NamespaceDelete.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=430,
  serialized_end=461,
)

_NAMESPACECREATE_LABELSENTRY.containing_type = _NAMESPACECREATE
_NAMESPACECREATE.fields_by_name['labels'].message_type = _NAMESPACECREATE_LABELSENTRY
_NAMESPACEUPDATE_LABELSENTRY.containing_type = _NAMESPACEUPDATE
_NAMESPACEUPDATE.fields_by_name['labels'].message_type = _NAMESPACEUPDATE_LABELSENTRY
DESCRIPTOR.message_types_by_name['NamespaceCreate'] = _NAMESPACECREATE
DESCRIPTOR.message_types_by_name['NamespaceUpdate'] = _NAMESPACEUPDATE
DESCRIPTOR.message_types_by_name['NamespaceDelete'] = _NAMESPACEDELETE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NamespaceCreate = _reflection.GeneratedProtocolMessageType('NamespaceCreate', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _NAMESPACECREATE_LABELSENTRY,
    '__module__' : 'containerd.events.namespace_pb2'
    # @@protoc_insertion_point(class_scope:containerd.events.NamespaceCreate.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _NAMESPACECREATE,
  '__module__' : 'containerd.events.namespace_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.NamespaceCreate)
  })
_sym_db.RegisterMessage(NamespaceCreate)
_sym_db.RegisterMessage(NamespaceCreate.LabelsEntry)

NamespaceUpdate = _reflection.GeneratedProtocolMessageType('NamespaceUpdate', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _NAMESPACEUPDATE_LABELSENTRY,
    '__module__' : 'containerd.events.namespace_pb2'
    # @@protoc_insertion_point(class_scope:containerd.events.NamespaceUpdate.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _NAMESPACEUPDATE,
  '__module__' : 'containerd.events.namespace_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.NamespaceUpdate)
  })
_sym_db.RegisterMessage(NamespaceUpdate)
_sym_db.RegisterMessage(NamespaceUpdate.LabelsEntry)

NamespaceDelete = _reflection.GeneratedProtocolMessageType('NamespaceDelete', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACEDELETE,
  '__module__' : 'containerd.events.namespace_pb2'
  # @@protoc_insertion_point(class_scope:containerd.events.NamespaceDelete)
  })
_sym_db.RegisterMessage(NamespaceDelete)


DESCRIPTOR._options = None
_NAMESPACECREATE_LABELSENTRY._options = None
_NAMESPACEUPDATE_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
