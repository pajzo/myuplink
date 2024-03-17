"""Test myuplink data models."""

import pytest
from aiohttp import ClientSession

from src.myuplink.auth import Auth
from src.myuplink import MyUplinkAPI

from .conftest import load_json_fixture
from .const import API_ENDPOINT


@pytest.mark.asyncio
async def test_systems(aiosession: ClientSession, aioresponse):
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
