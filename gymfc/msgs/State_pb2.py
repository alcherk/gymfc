# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: State.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='State.proto',
  package='gymfc.msgs',
  syntax='proto2',
  serialized_pb=_b('\n\x0bState.proto\x12\ngymfc.msgs\"\xc3\x03\n\x05State\x12\x10\n\x08sim_time\x18\x01 \x02(\x02\x12$\n\x18imu_angular_velocity_rpy\x18\x02 \x03(\x02\x42\x02\x10\x01\x12\'\n\x1bimu_linear_acceleration_xyz\x18\x03 \x03(\x02\x42\x02\x10\x01\x12 \n\x14imu_orientation_quat\x18\x04 \x03(\x02\x42\x02\x10\x01\x12&\n\x1a\x65sc_motor_angular_velocity\x18\x05 \x03(\x02\x42\x02\x10\x01\x12\x1b\n\x0f\x65sc_temperature\x18\x06 \x03(\x02\x42\x02\x10\x01\x12\x17\n\x0b\x65sc_current\x18\x07 \x03(\x02\x42\x02\x10\x01\x12\x17\n\x0b\x65sc_voltage\x18\x08 \x03(\x02\x42\x02\x10\x01\x12\x15\n\tesc_force\x18\t \x03(\x02\x42\x02\x10\x01\x12\x16\n\nesc_torque\x18\n \x03(\x02\x42\x02\x10\x01\x12\x14\n\x0cvbat_voltage\x18\x0b \x01(\x02\x12\x14\n\x0cvbat_current\x18\x0c \x01(\x02\x12\x31\n\x0bstatus_code\x18\r \x02(\x0e\x32\x1c.gymfc.msgs.State.StatusCode\x12\x11\n\x05\x66orce\x18\x0e \x03(\x02\x42\x02\x10\x01\"\x1f\n\nStatusCode\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STATE_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='gymfc.msgs.State.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=448,
  serialized_end=479,
)
_sym_db.RegisterEnumDescriptor(_STATE_STATUSCODE)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='gymfc.msgs.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sim_time', full_name='gymfc.msgs.State.sim_time', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imu_angular_velocity_rpy', full_name='gymfc.msgs.State.imu_angular_velocity_rpy', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='imu_linear_acceleration_xyz', full_name='gymfc.msgs.State.imu_linear_acceleration_xyz', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='imu_orientation_quat', full_name='gymfc.msgs.State.imu_orientation_quat', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='esc_motor_angular_velocity', full_name='gymfc.msgs.State.esc_motor_angular_velocity', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='esc_temperature', full_name='gymfc.msgs.State.esc_temperature', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='esc_current', full_name='gymfc.msgs.State.esc_current', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='esc_voltage', full_name='gymfc.msgs.State.esc_voltage', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='esc_force', full_name='gymfc.msgs.State.esc_force', index=8,
      number=9, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='esc_torque', full_name='gymfc.msgs.State.esc_torque', index=9,
      number=10, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='vbat_voltage', full_name='gymfc.msgs.State.vbat_voltage', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vbat_current', full_name='gymfc.msgs.State.vbat_current', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_code', full_name='gymfc.msgs.State.status_code', index=12,
      number=13, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='force', full_name='gymfc.msgs.State.force', index=13,
      number=14, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATE_STATUSCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=479,
)

_STATE.fields_by_name['status_code'].enum_type = _STATE_STATUSCODE
_STATE_STATUSCODE.containing_type = _STATE
DESCRIPTOR.message_types_by_name['State'] = _STATE

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(
  DESCRIPTOR = _STATE,
  __module__ = 'State_pb2'
  # @@protoc_insertion_point(class_scope:gymfc.msgs.State)
  ))
_sym_db.RegisterMessage(State)


_STATE.fields_by_name['imu_angular_velocity_rpy'].has_options = True
_STATE.fields_by_name['imu_angular_velocity_rpy']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_STATE.fields_by_name['imu_linear_acceleration_xyz'].has_options = True
_STATE.fields_by_name['imu_linear_acceleration_xyz']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_STATE.fields_by_name['imu_orientation_quat'].has_options = True
_STATE.fields_by_name['imu_orientation_quat']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_STATE.fields_by_name['esc_motor_angular_velocity'].has_options = True
_STATE.fields_by_name['esc_motor_angular_velocity']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_STATE.fields_by_name['esc_temperature'].has_options = True
_STATE.fields_by_name['esc_temperature']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_STATE.fields_by_name['esc_current'].has_options = True
_STATE.fields_by_name['esc_current']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_STATE.fields_by_name['esc_voltage'].has_options = True
_STATE.fields_by_name['esc_voltage']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_STATE.fields_by_name['esc_force'].has_options = True
_STATE.fields_by_name['esc_force']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_STATE.fields_by_name['esc_torque'].has_options = True
_STATE.fields_by_name['esc_torque']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_STATE.fields_by_name['force'].has_options = True
_STATE.fields_by_name['force']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
