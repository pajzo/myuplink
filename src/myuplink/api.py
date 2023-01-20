from typing import List

from .auth import Auth
from .models import System, Device


class MyUplinkAPI:
    """Class to communicate with the myUplink API."""

    def __init__(self, auth: Auth):
        """Initialize the API and store the auth so we can make requests."""
        self.auth = auth

    async def async_get_systems(self) -> List[System]:
        """Return systems."""
        resp = await self.auth.request("get", "v2/systems/me")
        resp.raise_for_status()
        json = await resp.json()
        array = json["systems"]        
        return [System(system_data) for system_data in array]

    async def async_get_device(self, device_id) -> Device:
        """Return the device."""
        resp = await self.auth.request("get", f"v2/devices/{device_id}")
        resp.raise_for_status()
        return Device(await resp.json(), self.auth)