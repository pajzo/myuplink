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
            print(system.id)
            print(system.name)
            print(system.hasAlarm)

            for sysDevice in system.devices:
                device = await api.async_get_device(sysDevice.deviceId)
                print(f"Device id: {device.id}")
                print(f"Device productName: {device.productName}")
                print(f"Device productSerialNumber: {device.productSerialNumber}")
                print(f"Device productCurrentFirmware: {device.firmwareCurrent}")
                print(f"Device productDesiredFirmware: {device.firmwareDesired}")
                print(f"Device connectionState: {device.connectionState}")

                zones = await api.async_get_smart_home_zones(sysDevice.deviceId)
                if len(zones) == 0:
                    print()
                    print("No zones defined on device")
                else:
                    for zone in zones:
                        print("")
                        print(f"Zone id: {zone.zone_id}")
                        print(f"Zone name: {zone.name}")
                print()


asyncio.run(main())
