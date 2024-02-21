"""Define the MyUplinkAPI class."""

from .auth import AbstractAuth
from .models import System, SystemNotification, Device, DevicePoint, Paging, Zone


class MyUplinkAPI:
    """Class to communicate with the myUplink API."""

    def __init__(self, auth: AbstractAuth):
        """Initialize the API and store the auth so we can make requests."""
        self.auth = auth

    async def async_ping(self) -> bool:
        """Return true or false, depending on ping status."""

        resp = await self.auth.request("get", "v2/ping", include_access_token=False)

        if 200 <= resp.status < 300:
            return True
        else:
            return False

    async def async_ping_protected(self) -> bool:
        """Return true or false, depending on protected ping status."""

        resp = await self.auth.request("get", "v2/protected-ping")

        if 200 <= resp.status < 300:
            return True
        else:
            return False

    async def async_get_systems(self) -> list[System]:
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

    async def async_get_device_points(
        self, device_id, language: str = "en-GB"
    ) -> list[DevicePoint]:
        """Return device points."""
        array = await self.async_get_device_points_json(device_id, language)
        return [DevicePoint(point_data) for point_data in array]

    async def async_get_device_points_json(
        self, device_id, language: str = "en-GB"
    ) -> dict:
        """Return device points as json."""
        headers = {"Accept-Language": language}
        resp = await self.auth.request(
            "get", f"v2/devices/{device_id}/points", headers=headers
        )
        resp.raise_for_status()
        return await resp.json()

    async def async_set_device_points(self, device_id, data: dict) -> dict:
        """Return device points."""
        headers = {"Content-Type": "application/json-patch+json"}
        resp = await self.auth.request(
            "patch", f"v2/devices/{device_id}/points", json=data, headers=headers
        )
        resp.raise_for_status()
        array = await resp.json()
        return array

    async def async_get_system_notifications(
        self,
        system_id,
        only_active: bool = True,
        page: int = 1,
        items_per_page=10,
        language: str = "en-GB",
    ) -> Paging[SystemNotification]:
        """Return device points."""
        json = await self.async_get_system_notifications_json(
            system_id=system_id,
            only_active=only_active,
            page=page,
            items_per_page=items_per_page,
            language=language,
        )

        json_array = json["notifications"]
        model_array = [SystemNotification(notification) for notification in json_array]

        paging = Paging(
            page_number=json["page"],
            items_per_page=json["itemsPerPage"],
            total_items=json["numItems"],
            items=model_array,
        )

        return paging

    async def async_get_system_notifications_json(
        self,
        system_id,
        only_active: bool = True,
        page: int = 1,
        items_per_page=10,
        language: str = "en-GB",
    ) -> dict:
        """Return system notifications as json."""
        headers = {"Accept-Language": language}

        active_suffix = ""
        if only_active:
            active_suffix = "/active"

        resp = await self.auth.request(
            "get",
            f"v2/systems/{system_id}/notifications{active_suffix}"
            f"?page={page}&itemsPerPage={items_per_page}",
            headers=headers,
        )
        resp.raise_for_status()
        return await resp.json()

    async def async_get_smart_home_mode_json(self, system_id: str) -> dict:
        """Return smart_home_mode as json."""
        resp = await self.auth.request("get", f"v2/systems/{system_id}/smart-home-mode")
        resp.raise_for_status()
        return await resp.json()

    async def async_get_smart_home_mode(self, system_id: str) -> dict:
        """Return smart_home_mode."""
        json = await self.async_get_smart_home_mode_json(system_id)
        return json

    async def async_set_smart_home_mode(self, system_id: str, data: dict) -> dict:
        """Return device points."""
        headers = {"Content-Type": "application/json-patch+json"}
        resp = await self.auth.request(
            "put", f"v2/devices/{system_id}/smart-home-mode", json=data, headers=headers
        )
        resp.raise_for_status()
        array = await resp.json()
        return array

    async def async_get_smart_home_categories_json(self, device_id: str) -> dict:
        """Return smart home categories for device as json."""
        resp = await self.auth.request(
            "get", f"v2/devices/{device_id}/smart-home-categories"
        )
        resp.raise_for_status()
        return await resp.json()

    async def async_get_smart_home_categories(self, device_id: str) -> dict:
        """Return smart home categories for device."""
        data = await self.async_get_smart_home_categories_json(device_id)
        return data

    async def async_get_smart_home_zones_json(self, device_id: str) -> dict:
        """Return smart home zones for device as json."""
        resp = await self.auth.request(
            "get", f"v2/devices/{device_id}/smart-home-zones"
        )
        resp.raise_for_status()
        return await resp.json()

    async def async_get_smart_home_zones(self, device_id: str) -> list[Zone]:
        """Return smart home zones for device."""
        data = await self.async_get_smart_home_zones_json(device_id)
        return [Zone(zone_data) for zone_data in data]
