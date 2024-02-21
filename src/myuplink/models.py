from typing import TypeVar, Generic, List
from datetime import datetime
from enum import Enum

T = TypeVar("T")


class Paging(Generic[T]):
    def __init__(
        self, page_number: int, items_per_page: int, total_items: int, items: List[T]
    ):
        """Initialize a paging object."""
        self.page_number = page_number
        self.items_per_page = items_per_page
        self.total_items = total_items
        self.items = items


class SystemDevice:
    def __init__(self, raw_data: dict):
        """Initialize a system device object."""
        self.raw_data = raw_data

    @property
    def id(self) -> str:
        """Return the ID of the device."""
        return self.raw_data["id"]

    @property
    def deviceId(self) -> str:
        """Return the ID of the device. Deprecated 2024-04-30."""
        return self.id

    @property
    def product_name(self) -> str:
        """Return the system name."""
        return self.raw_data["product"]["name"]

    @property
    def product_serial_number(self) -> str:
        """Return the product serial number."""
        return self.raw_data["product"]["serialNumber"]

    @property
    def current_fw_version(self) -> str:
        """Return the current firmware version."""
        return self.raw_data["currentFwVersion"]

    @property
    def raw(self) -> dict:
        return self.raw_data


class SystemNotificationStatus(Enum):
    NoStatus = 0
    Active = 1
    DismissedByDevice = 2
    ResetByUserOnDevice = 3
    ResetByUserFromCloud = 4


class SystemNotification:
    def __init__(self, raw_data: dict):
        """Initialize a system notification object."""
        self.raw_data = raw_data

    @property
    def notification_id(self) -> str:
        """Return the ID of the notification."""
        return self.raw_data["id"]

    @property
    def notificationId(self) -> str:
        """Return the ID of the notification. Deprecated 2024-04-30."""
        return self.notification_id

    @property
    def device_id(self) -> str:
        """Return the device ID of the notification."""
        return self.raw_data["deviceId"]

    @property
    def created(self) -> datetime:
        """Return the date and time of the notification."""
        return datetime.strptime(
            self.raw_data["createdDatetime"][:-2], "%Y-%m-%dT%H:%M:%S"
        )

    @property
    def alarm_number(self) -> int:
        """Return the alarm number."""
        return self.raw_data["alarmNumber"]

    @property
    def alarmNumber(self) -> int:
        """Return the alarm number. Deprecated 2024-04-30"""
        return self.alarm_number

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
    def equip_name(self) -> str:
        """Return the equipName of the notification."""
        return self.raw_data["equipName"]

    @property
    def equipName(self) -> str:
        """Return the equipName of the notification. Deprecated 2024-04-30."""
        return self.equip_name

    @property
    def raw(self) -> dict:
        return self.raw_data


class System:
    def __init__(self, raw_data: dict):
        """Initialize a system object."""
        self.raw_data = raw_data

    @property
    def system_id(self) -> str:
        """Return the system ID."""
        return self.raw_data["systemId"]

    @property
    def id(self) -> str:
        """Return the ID of the system. Deprecated 2024-04-30"""
        return self.system_id

    @property
    def name(self) -> str:
        """Return the name of the system."""
        return self.raw_data["name"]

    @property
    def has_alarm(self) -> bool:
        """Return if the system has alarm."""
        return self.raw_data["hasAlarm"]

    @property
    def hasAlarm(self) -> bool:
        """Return if the system has alarm. Deprecated 2024-04-30"""
        return self.has_alarm

    @property
    def security_level(self) -> str:
        """ "Return the security level."""
        return self.raw_data["securityLevel"]

    @property
    def country(self) -> str:
        """ "Return the country."""
        return self.raw_data["country"]

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


class Device:
    def __init__(self, raw_data: dict):
        """Initialize a device object."""
        self.raw_data = raw_data

    @property
    def id(self) -> str:
        """Return the ID of the device."""
        return self.raw_data["id"]

    @property
    def product_name(self) -> str:
        """Return the name of the device product."""
        return self.raw_data["product"]["name"]

    @property
    def productName(self) -> str:
        """Return the name of the device product. Deprecated 2024-04-30."""
        return self.product_name

    @property
    def product_serial_number(self) -> str:
        """Return the serialno. of the device product."""
        return self.raw_data["product"]["serialNumber"]

    @property
    def productSerialNumber(self) -> str:
        """Return the serialno. of the device product. Deprecated 2024-04-30."""
        return self.product_serial_number

    @property
    def curret_firmware_version(self) -> str:
        """Return the current firmware version."""
        return self.raw_data["firmware"]["currentFwVersion"]

    @property
    def firmwareCurrent(self) -> str:
        """Return the current firmware version. Deprecated 2024-04-30."""
        return self.curret_firmware_version

    @property
    def desired_firmware_version(self) -> str:
        """Return the desired firmware version."""
        return self.raw_data["firmware"]["desiredFwVersion"]

    @property
    def firmwareDesired(self) -> str:
        """Return the desired firmware version. Deprecated 2024-04-30."""
        return self.desired_firmware_version

    @property
    def available_features(self) -> dict[str, bool]:
        """Return dict with available features."""
        return self.raw_data["available_features"]

    @property
    def firmwareDesired(self) -> str:
        """Return the desired firmware version. Deprecated 2024-04-30."""
        return self.desired_firmware_version

    @property
    def available_features(self) -> dict[str, bool]:
        """Return dict with available features."""
        return self.raw_data["available_features"]

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


class EnumValue:
    @property
    def value(self) -> str | None:
        return self.raw_data["value"]

    @property
    def text(self) -> str | None:
        return self.raw_data["text"]

    @property
    def icon(self) -> str | None:
        return self.raw_data["icon"]


class DevicePoint:
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
    def smart_home_categories(self) -> List[str]:
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


class Zone:
    """Define Zone object."""

    def __init__(self, raw_data: dict):
        """Init the Zone object."""
        self.raw_data = raw_data

    @property
    def zone_id(self) -> str | None:
        """Return the zone id."""
        return self.raw_data["zoneId"]

    @property
    def name_id(self) -> str | None:
        """Return the name."""
        return self.raw_data["name"]

    @property
    def command_only(self) -> bool:
        """Return command_only."""
        return self.raw_data["commandOnly"]

    @property
    def supported_modes(self) -> str | None:
        """Return the supported modes."""
        return self.raw_data["supportedModes"]

    @property
    def mode(self) -> str | None:
        """Return the mode."""
        return self.raw_data["mode"]

    @property
    def temperature(self) -> float | None:
        """Return the temperature."""
        return self.raw_data["temperature"]

    @property
    def setpoint(self) -> float | None:
        """Return the setpoint."""
        return self.raw_data["setpoint"]

    @property
    def setpoint_heat(self) -> float | None:
        """Return the heat setpoint."""
        return self.raw_data["setpointHeat"]

    @property
    def setpoint_cool(self) -> float | None:
        """Return the coolsetpoint."""
        return self.raw_data["setpointCool"]

    @property
    def setpoint_range_max(self) -> int | None:
        """Return the max range setpoint."""
        return self.raw_data["setpointRangeMax"]

    @property
    def setpoint_range_min(self) -> int | None:
        """Return the min range setpoint."""
        return self.raw_data["setpointRangeMin"]

    @property
    def is_celcius(self) -> bool:
        """Return is celcius."""
        return self.raw_data["isCelcius"]

    @property
    def indoor_co2(self) -> int | None:
        """Return the indoor CO2 level."""
        return self.raw_data["indoorCo2"]

    @property
    def indoor_humidity(self) -> float | None:
        """Return the indoor humidity."""
        return self.raw_data["indoorHumidity"]

    @property
    def raw(self) -> dict:
        """Return the raw data."""
        return self.raw_data
