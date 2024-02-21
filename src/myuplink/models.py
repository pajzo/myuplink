from typing import TypeVar, Generic, List
from datetime import datetime
from enum import Enum

T = TypeVar('T')

class Paging(Generic[T]):

    def __init__(self, page_number: int, items_per_page: int, total_items: int, items: List[T]):
        """Initialize a paging object."""
        self.page_number = page_number
        self.items_per_page = items_per_page
        self.total_items = total_items
        self.items = items

class SystemDevice():

    def __init__(self, raw_data: dict):
        """Initialize a system device object."""
        self.raw_data = raw_data

    @property
    def deviceId(self) -> str:
        """Return the ID of the device."""
        return self.raw_data["id"]

    @property
    def raw(self) -> dict:
        return self.raw_data

class SystemNotificationStatus(Enum):
    NoStatus = 0
    Active = 1
    DismissedByDevice = 2
    ResetByUserOnDevice = 3
    ResetByUserFromCloud = 4

class SystemNotification():

    def __init__(self, raw_data: dict):
        """Initialize a system notification object."""
        self.raw_data = raw_data

    @property
    def notificationId(self) -> str:
        """Return the ID of the notification."""
        return self.raw_data["id"]

    @property
    def created(self) -> datetime:
        """Return the date and time of the notification."""
        return datetime.strptime(self.raw_data["createdDatetime"][:-2], "%Y-%m-%dT%H:%M:%S")

    @property
    def alarmNumber(self) -> int:
        """Return the alarm number."""
        return self.raw_data["id"]

    @property
    def severity(self) -> int:
        """Return the severity of the notification."""
        return self.raw_data["severity"]

    @property
    def status(self) -> SystemNotificationStatus | None:
        """Return the status of the notification."""
        status_str = self.raw_data.get("status", "Unknown").replace("None", "NoStatus")

        if status_str in SystemNotificationStatus.__members__:
            return SystemNotificationStatus[status_str]
        else:
            return None

    @property
    def header(self) -> str:
        """Return the header of the notification."""
        return self.raw_data["header"]

    @property
    def description(self) -> str:
        """Return the description of the notification."""
        return self.raw_data["description"]

    @property
    def equipName(self) -> str:
        """Return the equipName of the notification."""
        return self.raw_data["equipName"]

    @property
    def raw(self) -> dict:
        return self.raw_data

class System():

    def __init__(self, raw_data: dict):
        """Initialize a system object."""
        self.raw_data = raw_data

    @property
    def id(self) -> str:
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

    @property
    def raw(self) -> dict:
        return self.raw_data

class DeviceConnectionState(Enum):
    Disconnected = 0
    Connected = 1

class Device():

    def __init__(self, raw_data: dict):
        """Initialize a device object."""
        self.raw_data = raw_data

    @property
    def id(self) -> str:
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
    def connectionState(self) -> DeviceConnectionState | None:
        """Return the connection state."""
        connection_state_str = self.raw_data.get("connectionState", "Unknown")

        if connection_state_str in DeviceConnectionState.__members__:
            return DeviceConnectionState[connection_state_str]
        else:
            return None

    @property
    def raw(self) -> dict:
        return self.raw_data

class EnumValue():

    @property
    def value(self) -> str | None:
        return self.raw_data["value"]
    @property
    def text(self) -> str | None:
        return self.raw_data["text"]
    @property
    def icon(self) -> str | None:
        return self.raw_data["icon"]

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
    def value(self) -> str | float | int | None:
        return self.raw_data["value"]

    @value.setter
    def value(self, new_value: str | float | int | None):
        self.raw_data["value"] = new_value

    @property
    def min_value(self) -> float | None:
        return self.raw_data["minValue"]

    @property
    def max_value(self) -> float | None:
        return self.raw_data["maxValue"]

    @property
    def step_value(self) -> float | None:
        return self.raw_data["stepValue"]

    @property
    def scale_value(self) -> float | None:
        return self.raw_data["scaleValue"]

    @property
    def enum_values_list(self) -> List[EnumValue]:
        return [EnumValue(enum_data) for enum_data in self.raw_data["enumValues"]]

    @property
    def enum_values(self) -> List[EnumValue]:
        return self.raw_data["enumValues"]

    @property
    def smart_home_categories(self):
        return self.raw_data["smartHomeCategories"]

    @property
    def writable(self) -> bool:
        return self.raw_data["writable"]

    @property
    def zone_id(self):
        return self.raw_data["zoneId"]

    @property
    def raw(self) -> dict:
        return self.raw_data
