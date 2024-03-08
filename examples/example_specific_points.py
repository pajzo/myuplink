"""List defined zones."""
import asyncio
import aiohttp

from my_token import MY_TOKEN

from myuplink.auth import Auth
from myuplink import MyUplinkAPI

PARAMETERS = ["40004", "40940", "40005"]


async def main():
    """Connect and print test data."""
    async with aiohttp.ClientSession() as session:
        auth = Auth(
            session,
            "https://api.myuplink.com",
            MY_TOKEN,
        )
        api = MyUplinkAPI(auth)

        systems = await api.async_get_systems()
        for system in systems:
            print(f"System id: {system.id}")
            print(f"System name: {system.name}")

            print(f"No of devices in system: {len(system.devices)}")
            for sys_device in system.devices:
                device = await api.async_get_device(sys_device.deviceId)
                print(device.id)
                print(device.productName)
                print(device.productSerialNumber)
                print(device.firmwareCurrent)
                print(device.firmwareDesired)
                print(device.connectionState)

                points = await api.async_get_device_points(
                    sys_device.deviceId, points=PARAMETERS
                )
                for point in points:
                    print(
                        f"{point.parameter_id} | {point.parameter_name} | {point.value}"
                    )
                print()


asyncio.run(main())
