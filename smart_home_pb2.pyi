from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActuatorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LAMP: _ClassVar[ActuatorType]
    THERMOSTAT: _ClassVar[ActuatorType]
    IRRIGATOR: _ClassVar[ActuatorType]

class SensorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PRESENCE: _ClassVar[SensorType]
    TEMPERATURE: _ClassVar[SensorType]
    HUMIDITY: _ClassVar[SensorType]
LAMP: ActuatorType
THERMOSTAT: ActuatorType
IRRIGATOR: ActuatorType
PRESENCE: SensorType
TEMPERATURE: SensorType
HUMIDITY: SensorType

class LampRequest(_message.Message):
    __slots__ = ["state"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: bool
    def __init__(self, state: bool = ...) -> None: ...

class LampResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class TemperatureRequest(_message.Message):
    __slots__ = ["temperature"]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    temperature: float
    def __init__(self, temperature: _Optional[float] = ...) -> None: ...

class TemperatureResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ActuatorRequest(_message.Message):
    __slots__ = ["type", "value"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: ActuatorType
    value: str
    def __init__(self, type: _Optional[_Union[ActuatorType, str]] = ..., value: _Optional[str] = ...) -> None: ...

class SensorRequest(_message.Message):
    __slots__ = ["type"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: SensorType
    def __init__(self, type: _Optional[_Union[SensorType, str]] = ...) -> None: ...

class ObjectValue(_message.Message):
    __slots__ = ["type", "value"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: str
    value: str
    def __init__(self, type: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ObjectResponse(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[ObjectValue]
    def __init__(self, values: _Optional[_Iterable[_Union[ObjectValue, _Mapping]]] = ...) -> None: ...
