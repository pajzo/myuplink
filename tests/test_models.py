"""Test myuplink data models."""

import pytest
from aiohttp import ClientSession

from src.myuplink.auth import Auth
from src.myuplink import MyUplinkAPI

from .conftest import load_json_fixture
from .const import API_ENDPOINT


@pytest.mark.asyncio
async def test_system(aiosession: ClientSession, aioresponse):
    """Test System model."""
    aioresponse.get(
        f"{API_ENDPOINT}/v2/systems/me", payload=load_json_fixture("systems.json")
    )
    auth = Auth(aiosession, API_ENDPOINT, "token")
    api = MyUplinkAPI(auth)
    systems = await api.async_get_systems()
    assert len(systems) == 1
    system = systems[0]
    assert system.system_id == "123456-7890-1234"
    assert system.name == "Batcave"
    assert len(system.devices) == 1
    device = system.devices[0]
    assert device.id == "batman-r-1234-20240201-123456-aa-bb-cc-dd-ee-ff"
    await aiosession.close()


@pytest.mark.asyncio
async def test_points(aiosession: ClientSession, aioresponse):
    """Test DevicePoint model."""
    aioresponse.get(
        f"{API_ENDPOINT}/v2/devices/dummy/points",
        payload=load_json_fixture("device_points.json"),
    )
    auth = Auth(aiosession, API_ENDPOINT, "token")
    api = MyUplinkAPI(auth)
    device_points = await api.async_get_device_points("dummy")
    assert len(device_points) == 4
    device_point = device_points[0]
    assert device_point.category == "NIBEF F730 CU 3x400V"
    assert device_point.parameter_id == "40004"
    assert device_point.value == -9.3
    await aiosession.close()
