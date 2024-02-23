"""List defined zones."""
import asyncio
import aiohttp

from myuplink.auth import Auth
from myuplink import MyUplinkAPI
from my_token import MY_TOKEN


async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(
            session,
            "https://api.myuplink.com",
            MY_TOKEN,
        )
        api = MyUplinkAPI(auth)

        systems = await api.async_get_systems()
        for system in systems:
            print("---------" + str(len(systems)))
            print(system.id)
            print(system.name)
            print(system.hasAlarm)

            print(systems)
            for sysDevice in system.devices:
                print(len(systems))
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
                    for enum_value in point.enum_values_list:
                        print(point.parameter_name + " | enum: " + enum_value.text)


asyncio.run(main())
