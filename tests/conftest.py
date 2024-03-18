"""Common fixtures for myuplink tests."""

import os
import json

from aiohttp import ClientSession
import pytest_asyncio
from aioresponses import aioresponses
from .const import API_ENDPOINT


def load_json_fixture(filename: str) -> dict:
    """Fixture for loading a json file."""
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures", filename), encoding="utf-8"
    ) as f:
        return json.load(f)


@pytest_asyncio.fixture(name="aioresponse")
async def aioresponse_fixture():
    """Fixture for aioresponses."""
    with aioresponses() as m:
        yield m


@pytest_asyncio.fixture
async def aiosession() -> ClientSession:
    """Fixture for client session."""
    return ClientSession(API_ENDPOINT)
