from typing import List

from auth import Auth

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


class Device(Auth):

    def __init__(self, raw_data: dict, auth: Auth):
        """Initialize a device object."""
        self.raw_data = raw_data
        self.auth = auth

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

    async def async_update(self):
        """Update the device data."""
        resp = await self.auth.request("get", f"v2/devices/{self.id}")
        resp.raise_for_status()
        self.raw_data = await resp.json()        