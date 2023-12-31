# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import smart_home_pb2 as smart__home__pb2


class LampServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetState = channel.unary_unary(
                '/smart_home.LampService/SetState',
                request_serializer=smart__home__pb2.LampRequest.SerializeToString,
                response_deserializer=smart__home__pb2.LampResponse.FromString,
                )
        self.GetState = channel.unary_unary(
                '/smart_home.LampService/GetState',
                request_serializer=smart__home__pb2.Empty.SerializeToString,
                response_deserializer=smart__home__pb2.LampResponse.FromString,
                )


class LampServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LampServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetState,
                    request_deserializer=smart__home__pb2.LampRequest.FromString,
                    response_serializer=smart__home__pb2.LampResponse.SerializeToString,
            ),
            'GetState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetState,
                    request_deserializer=smart__home__pb2.Empty.FromString,
                    response_serializer=smart__home__pb2.LampResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'smart_home.LampService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LampService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smart_home.LampService/SetState',
            smart__home__pb2.LampRequest.SerializeToString,
            smart__home__pb2.LampResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smart_home.LampService/GetState',
            smart__home__pb2.Empty.SerializeToString,
            smart__home__pb2.LampResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ThermostatServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetTemperature = channel.unary_unary(
                '/smart_home.ThermostatService/SetTemperature',
                request_serializer=smart__home__pb2.TemperatureRequest.SerializeToString,
                response_deserializer=smart__home__pb2.TemperatureResponse.FromString,
                )
        self.UpdateDesiredTemperature = channel.unary_unary(
                '/smart_home.ThermostatService/UpdateDesiredTemperature',
                request_serializer=smart__home__pb2.TemperatureRequest.SerializeToString,
                response_deserializer=smart__home__pb2.TemperatureResponse.FromString,
                )
        self.GetTemperature = channel.unary_unary(
                '/smart_home.ThermostatService/GetTemperature',
                request_serializer=smart__home__pb2.Empty.SerializeToString,
                response_deserializer=smart__home__pb2.TemperaturaResponseNumber.FromString,
                )


class ThermostatServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetTemperature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDesiredTemperature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTemperature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ThermostatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTemperature,
                    request_deserializer=smart__home__pb2.TemperatureRequest.FromString,
                    response_serializer=smart__home__pb2.TemperatureResponse.SerializeToString,
            ),
            'UpdateDesiredTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDesiredTemperature,
                    request_deserializer=smart__home__pb2.TemperatureRequest.FromString,
                    response_serializer=smart__home__pb2.TemperatureResponse.SerializeToString,
            ),
            'GetTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTemperature,
                    request_deserializer=smart__home__pb2.Empty.FromString,
                    response_serializer=smart__home__pb2.TemperaturaResponseNumber.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'smart_home.ThermostatService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ThermostatService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smart_home.ThermostatService/SetTemperature',
            smart__home__pb2.TemperatureRequest.SerializeToString,
            smart__home__pb2.TemperatureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDesiredTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smart_home.ThermostatService/UpdateDesiredTemperature',
            smart__home__pb2.TemperatureRequest.SerializeToString,
            smart__home__pb2.TemperatureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smart_home.ThermostatService/GetTemperature',
            smart__home__pb2.Empty.SerializeToString,
            smart__home__pb2.TemperaturaResponseNumber.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class IrrigatorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetHumityIrrigator = channel.unary_unary(
                '/smart_home.IrrigatorService/SetHumityIrrigator',
                request_serializer=smart__home__pb2.HumidityRequest.SerializeToString,
                response_deserializer=smart__home__pb2.IrrigatorResponse.FromString,
                )
        self.SetStateIrrigator = channel.unary_unary(
                '/smart_home.IrrigatorService/SetStateIrrigator',
                request_serializer=smart__home__pb2.IrrigatorRequest.SerializeToString,
                response_deserializer=smart__home__pb2.IrrigatorResponse.FromString,
                )
        self.GetStateIrrigator = channel.unary_unary(
                '/smart_home.IrrigatorService/GetStateIrrigator',
                request_serializer=smart__home__pb2.Empty.SerializeToString,
                response_deserializer=smart__home__pb2.IrrigatorResponse.FromString,
                )


class IrrigatorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetHumityIrrigator(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetStateIrrigator(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStateIrrigator(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IrrigatorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetHumityIrrigator': grpc.unary_unary_rpc_method_handler(
                    servicer.SetHumityIrrigator,
                    request_deserializer=smart__home__pb2.HumidityRequest.FromString,
                    response_serializer=smart__home__pb2.IrrigatorResponse.SerializeToString,
            ),
            'SetStateIrrigator': grpc.unary_unary_rpc_method_handler(
                    servicer.SetStateIrrigator,
                    request_deserializer=smart__home__pb2.IrrigatorRequest.FromString,
                    response_serializer=smart__home__pb2.IrrigatorResponse.SerializeToString,
            ),
            'GetStateIrrigator': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStateIrrigator,
                    request_deserializer=smart__home__pb2.Empty.FromString,
                    response_serializer=smart__home__pb2.IrrigatorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'smart_home.IrrigatorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IrrigatorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetHumityIrrigator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smart_home.IrrigatorService/SetHumityIrrigator',
            smart__home__pb2.HumidityRequest.SerializeToString,
            smart__home__pb2.IrrigatorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetStateIrrigator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smart_home.IrrigatorService/SetStateIrrigator',
            smart__home__pb2.IrrigatorRequest.SerializeToString,
            smart__home__pb2.IrrigatorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStateIrrigator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smart_home.IrrigatorService/GetStateIrrigator',
            smart__home__pb2.Empty.SerializeToString,
            smart__home__pb2.IrrigatorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ClientServiceStub(object):
    """Service and messages to client interaction
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetActuatorValues = channel.unary_unary(
                '/smart_home.ClientService/SetActuatorValues',
                request_serializer=smart__home__pb2.ActuatorRequest.SerializeToString,
                response_deserializer=smart__home__pb2.ObjectResponse.FromString,
                )
        self.GetActuatorValues = channel.unary_unary(
                '/smart_home.ClientService/GetActuatorValues',
                request_serializer=smart__home__pb2.ActuatorRequest.SerializeToString,
                response_deserializer=smart__home__pb2.ObjectResponse.FromString,
                )
        self.GetSensorValues = channel.unary_stream(
                '/smart_home.ClientService/GetSensorValues',
                request_serializer=smart__home__pb2.SensorRequest.SerializeToString,
                response_deserializer=smart__home__pb2.ObjectResponse.FromString,
                )
        self.GetSensorValues2 = channel.unary_stream(
                '/smart_home.ClientService/GetSensorValues2',
                request_serializer=smart__home__pb2.SensorRequest.SerializeToString,
                response_deserializer=smart__home__pb2.ObjectResponse.FromString,
                )


class ClientServiceServicer(object):
    """Service and messages to client interaction
    """

    def SetActuatorValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActuatorValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSensorValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSensorValues2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetActuatorValues': grpc.unary_unary_rpc_method_handler(
                    servicer.SetActuatorValues,
                    request_deserializer=smart__home__pb2.ActuatorRequest.FromString,
                    response_serializer=smart__home__pb2.ObjectResponse.SerializeToString,
            ),
            'GetActuatorValues': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActuatorValues,
                    request_deserializer=smart__home__pb2.ActuatorRequest.FromString,
                    response_serializer=smart__home__pb2.ObjectResponse.SerializeToString,
            ),
            'GetSensorValues': grpc.unary_stream_rpc_method_handler(
                    servicer.GetSensorValues,
                    request_deserializer=smart__home__pb2.SensorRequest.FromString,
                    response_serializer=smart__home__pb2.ObjectResponse.SerializeToString,
            ),
            'GetSensorValues2': grpc.unary_stream_rpc_method_handler(
                    servicer.GetSensorValues2,
                    request_deserializer=smart__home__pb2.SensorRequest.FromString,
                    response_serializer=smart__home__pb2.ObjectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'smart_home.ClientService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClientService(object):
    """Service and messages to client interaction
    """

    @staticmethod
    def SetActuatorValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smart_home.ClientService/SetActuatorValues',
            smart__home__pb2.ActuatorRequest.SerializeToString,
            smart__home__pb2.ObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActuatorValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smart_home.ClientService/GetActuatorValues',
            smart__home__pb2.ActuatorRequest.SerializeToString,
            smart__home__pb2.ObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSensorValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/smart_home.ClientService/GetSensorValues',
            smart__home__pb2.SensorRequest.SerializeToString,
            smart__home__pb2.ObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSensorValues2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/smart_home.ClientService/GetSensorValues2',
            smart__home__pb2.SensorRequest.SerializeToString,
            smart__home__pb2.ObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
