from typing import List

from .auth import Auth
from .models import System, Device, DevicePoint


class MyUplinkAPI:
    """Class to communicate with the myUplink API."""

    def __init__(self, auth: Auth):
        """Initialize the API and store the auth so we can make requests."""
        self.auth = auth

    async def async_get_systems(self) -> List[System]:
        """Return systems."""
        json = await self.async_get_systems_json()
        array = json["systems"]        
        return [System(system_data) for system_data in array]

    async def async_get_systems_json(self) -> dict:
        """Return systems as json."""
        resp = await self.auth.request("get", "v2/systems/me")
        resp.raise_for_status()
        return await resp.json()

    async def async_get_device(self, device_id) -> Device:
        """Return the device."""
        json = await self.async_get_device_json(device_id)
        return Device(json)

    async def async_get_device_json(self, device_id) -> dict:
        """Return the device as json."""
        resp = await self.auth.request("get", f"v2/devices/{device_id}")
        resp.raise_for_status()
        return await resp.json()

    async def async_get_device_points(self, device_id, language: str = "en-GB") -> List[DevicePoint]:
        """Return device points."""
        array = await self.async_get_device_points_json(device_id, language)
        return [DevicePoint(point_data) for point_data in array]

    async def async_get_device_points_json(self, device_id, language: str = "en-GB") -> dict:
        """Return device points as json."""
        headers = {"Accept-Language": language}
        resp = await self.auth.request("get", f"v2/devices/{device_id}/points", headers=headers)
        resp.raise_for_status()
        return await resp.json()

    async def async_set_device_points(self, device_id, data: dict) -> dict:
        """Return device points."""
        resp = await self.auth.request("patch", f"v2/devices/{device_id}/points", json=data)
        resp.raise_for_status()
        array = await resp.json()
        return array
