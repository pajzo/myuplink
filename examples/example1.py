import asyncio
import aiohttp

from myuplink.auth import Auth
from myuplink.api import MyUplinkAPI


async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, "https://api.myuplink.com", "token")
        api = MyUplinkAPI(auth)

        systems = await api.async_get_systems()
        for system in systems:
            print(system.id)
            print(system.name)
            print(system.hasAlarm)

            for sysDevice in system.devices:
                device = await api.async_get_device(sysDevice.deviceId)
                print(device.id)
                print(device.productName)
                print(device.productSerialNumber)
                print(device.firmwareCurrent)
                print(device.firmwareDesired)
                print(device.connectionState)

                points = await api.async_get_device_points(sysDevice.deviceId)
                for point in points:
                    print(point.parameter_name)
                    print(point.timestamp)


asyncio.run(main())