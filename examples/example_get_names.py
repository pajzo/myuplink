"""List defined zones."""
import asyncio
import aiohttp

from myuplink import Auth
from myuplink import MyUplinkAPI
from myuplink import get_manufacturer, get_model, get_series, get_system_name


async def main():
    """Print name strings from system and devices."""
    async with aiohttp.ClientSession() as session:
        auth = Auth(
            session,
            "https://api.myuplink.com",
            "PUT_YOUR_TOKEN_HERE",
        )
        api = MyUplinkAPI(auth)

        systems = await api.async_get_systems()
        for system in systems:
            print()

            for device in system.devices:
                print(f"System name: {get_system_name(system)}")
                device = await api.async_get_device(device.id)
                print(f"Product name {device.product_name}")
                print(f"Model: {get_model(device)}")
                print(f"Manufacturer: {get_manufacturer(device)}")
                print(f"Series: {get_series(device)}")


asyncio.run(main())
