"""List defined zones."""
import asyncio
import aiohttp

from myuplink.auth import Auth
from myuplink import MyUplinkAPI


async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(
            session,
            "https://api.myuplink.com",
            "TOKEN",
        )
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

                zones = await api.async_get_smart_home_zones(sysDevice.deviceId)
                if len(zones) == 0:
                    print("No zones defined on device")
                else:
                    for zone in zones:
                        print(zone.zone_id)
                        print(zone.name)
                        print("")


asyncio.run(main())
