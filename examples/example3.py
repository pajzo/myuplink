import asyncio
import aiohttp

from myuplink.auth import Auth
from myuplink.api import MyUplinkAPI


async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, "https://api.myuplink.com", "token")
        api = MyUplinkAPI(auth)

        ping_result = await api.async_ping()
        print(ping_result)

        ping_protected_result = await api.async_ping_protected()
        print(ping_protected_result)

asyncio.run(main())