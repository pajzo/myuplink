from typing import List

from .auth import Auth

class SystemDevice():

    def __init__(self, raw_data: dict):
        """Initialize a system device object."""
        self.raw_data = raw_data

    @property
    def deviceId(self) -> int:
        """Return the ID of the device."""
        return self.raw_data["id"]


class System():

    def __init__(self, raw_data: dict):
        """Initialize a system object."""
        self.raw_data = raw_data

    @property
    def id(self) -> int:
        """Return the ID of the system."""
        return self.raw_data["systemId"]

    @property
    def name(self) -> str:
        """Return the name of the system."""
        return self.raw_data["name"]       

    @property
    def hasAlarm(self) -> bool:
        """Return if the system has alarm."""
        return self.raw_data["hasAlarm"]      

    @property
    def devices(self) -> List[SystemDevice]:
        """Return devices on the system."""
        return [SystemDevice(device_data) for device_data in self.raw_data["devices"]]


class Device():

    def __init__(self, raw_data: dict):
        """Initialize a device object."""
        self.raw_data = raw_data

    @property
    def id(self) -> int:
        """Return the ID of the device."""
        return self.raw_data["id"]

    @property
    def productName(self) -> str:
        """Return the name of the device product."""
        return self.raw_data["product"]["name"]

    @property
    def productSerialNumber(self) -> str:
        """Return the serialno. of the device product."""
        return self.raw_data["product"]["serialNumber"]

    @property
    def firmwareCurrent(self) -> str:
        """Return the current firmware version."""
        return self.raw_data["firmware"]["currentFwVersion"]        

    @property
    def firmwareDesired(self) -> str:
        """Return the desired firmware version."""
        return self.raw_data["firmware"]["desiredFwVersion"]       

    @property
    def connectionState(self) -> str:
        """Return the connection state."""
        return self.raw_data["connectionState"]


class DevicePoint():

    def __init__(self, raw_data: dict):
        """Initialize a device point."""
        self.raw_data = raw_data

    @property
    def category(self) -> str:
        return self.raw_data["category"]

    @property
    def parameter_id(self) -> str:
        return self.raw_data["parameterId"]

    @property
    def parameter_name(self) -> str:
        return self.raw_data["parameterName"]

    @property
    def parameter_unit(self) -> str:
        return self.raw_data["parameterUnit"]

    @property
    def timestamp(self) -> str:
        return self.raw_data["timestamp"]

    @property
    def value(self):
        return self.raw_data["value"]