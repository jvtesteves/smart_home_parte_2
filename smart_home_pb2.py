# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smart_home.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10smart_home.proto\x12\nsmart_home\"\x07\n\x05\x45mpty\"\x1c\n\x0bLampRequest\x12\r\n\x05state\x18\x01 \x01(\x08\"\x1f\n\x0cLampResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\")\n\x12TemperatureRequest\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\"&\n\x13TemperatureResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"0\n\x19TemperaturaResponseNumber\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\"#\n\x0fhumidityRequest\x12\x10\n\x08humidity\x18\x01 \x01(\x02\"!\n\x10IrrigatorRequest\x12\r\n\x05state\x18\x01 \x01(\x08\"$\n\x11IrrigatorResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"H\n\x0f\x41\x63tuatorRequest\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.smart_home.ActuatorType\x12\r\n\x05value\x18\x02 \x01(\t\"5\n\rSensorRequest\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.smart_home.SensorType\"*\n\x0bObjectValue\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"9\n\x0eObjectResponse\x12\'\n\x06values\x18\x01 \x03(\x0b\x32\x17.smart_home.ObjectValue*7\n\x0c\x41\x63tuatorType\x12\x08\n\x04LAMP\x10\x00\x12\x0e\n\nTHERMOSTAT\x10\x01\x12\r\n\tIRRIGATOR\x10\x02*9\n\nSensorType\x12\x0c\n\x08PRESENCE\x10\x00\x12\x0f\n\x0bTEMPERATURE\x10\x01\x12\x0c\n\x08HUMIDITY\x10\x02\x32\x89\x01\n\x0bLampService\x12?\n\x08SetState\x12\x17.smart_home.LampRequest\x1a\x18.smart_home.LampResponse\"\x00\x12\x39\n\x08GetState\x12\x11.smart_home.Empty\x1a\x18.smart_home.LampResponse\"\x00\x32\x95\x02\n\x11ThermostatService\x12S\n\x0eSetTemperature\x12\x1e.smart_home.TemperatureRequest\x1a\x1f.smart_home.TemperatureResponse\"\x00\x12]\n\x18UpdateDesiredTemperature\x12\x1e.smart_home.TemperatureRequest\x1a\x1f.smart_home.TemperatureResponse\"\x00\x12L\n\x0eGetTemperature\x12\x11.smart_home.Empty\x1a%.smart_home.TemperaturaResponseNumber\"\x00\x32\x84\x02\n\x10IrrigatorService\x12S\n\x12SetHumityIrrigator\x12\x1c.smart_home.IrrigatorRequest\x1a\x1d.smart_home.IrrigatorResponse\"\x00\x12R\n\x11SetStateIrrigator\x12\x1c.smart_home.IrrigatorRequest\x1a\x1d.smart_home.IrrigatorResponse\"\x00\x12G\n\x11GetStateIrrigator\x12\x11.smart_home.Empty\x1a\x1d.smart_home.IrrigatorResponse\"\x00\x32\xf7\x01\n\rClientService\x12L\n\x11SetActuatorValues\x12\x1b.smart_home.ActuatorRequest\x1a\x1a.smart_home.ObjectResponse\x12L\n\x11GetActuatorValues\x12\x1b.smart_home.ActuatorRequest\x1a\x1a.smart_home.ObjectResponse\x12J\n\x0fGetSensorValues\x12\x19.smart_home.SensorRequest\x1a\x1a.smart_home.ObjectResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'smart_home_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ACTUATORTYPE']._serialized_start=579
  _globals['_ACTUATORTYPE']._serialized_end=634
  _globals['_SENSORTYPE']._serialized_start=636
  _globals['_SENSORTYPE']._serialized_end=693
  _globals['_EMPTY']._serialized_start=32
  _globals['_EMPTY']._serialized_end=39
  _globals['_LAMPREQUEST']._serialized_start=41
  _globals['_LAMPREQUEST']._serialized_end=69
  _globals['_LAMPRESPONSE']._serialized_start=71
  _globals['_LAMPRESPONSE']._serialized_end=102
  _globals['_TEMPERATUREREQUEST']._serialized_start=104
  _globals['_TEMPERATUREREQUEST']._serialized_end=145
  _globals['_TEMPERATURERESPONSE']._serialized_start=147
  _globals['_TEMPERATURERESPONSE']._serialized_end=185
  _globals['_TEMPERATURARESPONSENUMBER']._serialized_start=187
  _globals['_TEMPERATURARESPONSENUMBER']._serialized_end=235
  _globals['_HUMIDITYREQUEST']._serialized_start=237
  _globals['_HUMIDITYREQUEST']._serialized_end=272
  _globals['_IRRIGATORREQUEST']._serialized_start=274
  _globals['_IRRIGATORREQUEST']._serialized_end=307
  _globals['_IRRIGATORRESPONSE']._serialized_start=309
  _globals['_IRRIGATORRESPONSE']._serialized_end=345
  _globals['_ACTUATORREQUEST']._serialized_start=347
  _globals['_ACTUATORREQUEST']._serialized_end=419
  _globals['_SENSORREQUEST']._serialized_start=421
  _globals['_SENSORREQUEST']._serialized_end=474
  _globals['_OBJECTVALUE']._serialized_start=476
  _globals['_OBJECTVALUE']._serialized_end=518
  _globals['_OBJECTRESPONSE']._serialized_start=520
  _globals['_OBJECTRESPONSE']._serialized_end=577
  _globals['_LAMPSERVICE']._serialized_start=696
  _globals['_LAMPSERVICE']._serialized_end=833
  _globals['_THERMOSTATSERVICE']._serialized_start=836
  _globals['_THERMOSTATSERVICE']._serialized_end=1113
  _globals['_IRRIGATORSERVICE']._serialized_start=1116
  _globals['_IRRIGATORSERVICE']._serialized_end=1376
  _globals['_CLIENTSERVICE']._serialized_start=1379
  _globals['_CLIENTSERVICE']._serialized_end=1626
# @@protoc_insertion_point(module_scope)
