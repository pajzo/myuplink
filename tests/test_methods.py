"""Test myuplink methods."""

# import aiohttp
# import asyncio
import pytest
# import pytest_asyncio

from src.myuplink.auth import Auth
from src.myuplink import MyUplinkAPI, get_manufacturer, get_model, get_system_name

from .conftest import load_json_fixture
from .const import API_ENDPOINT


@pytest.mark.asyncio
async def test_get_name(aiosession, aioresponse):
    """Test get_name method."""
    aioresponse.get(
        f"{API_ENDPOINT}/v2/systems/me", payload=load_json_fixture("systems.json")
    )
    auth = Auth(aiosession, API_ENDPOINT, "token")
    api = MyUplinkAPI(auth)
    systems = await api.async_get_systems()
    assert get_system_name(systems[0]) == "Batcave"
    await aiosession.close()


@pytest.mark.parametrize(
    ("fixture", "expected_model", "expected_manufacturer"),
    [
        ("batman", "F730", "Nibe"),
        ("robin", "S320", "Nibe"),
        ("joker", "SMO 20", "Nibe"),
    ],
)
@pytest.mark.asyncio
async def test_get_names(
    aiosession,
    aioresponse,
    fixture: str,
    expected_model: str,
    expected_manufacturer: str,
):
    """Test getting names methods."""
    aioresponse.get(
        f"{API_ENDPOINT}/v2/systems/me", payload=load_json_fixture("systems.json")
    )
    auth = Auth(aiosession, API_ENDPOINT, "token")
    api = MyUplinkAPI(auth)
    aioresponse.get(
        f"{API_ENDPOINT}/v2/devices/{fixture}",
        payload=load_json_fixture(f"dev_{fixture}.json"),
    )
    device = await api.async_get_device(fixture)
    assert get_model(device) == expected_model
    assert get_manufacturer(device) == expected_manufacturer
    await aiosession.close()
