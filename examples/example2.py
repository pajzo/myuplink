import asyncio
import aiohttp

from myuplink.auth import Auth
from myuplink.api import MyUplinkAPI


async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, "https://api.myuplink.com", "token")
        api = MyUplinkAPI(auth)

        paging = await api.async_get_system_notifications(system_id="xxxxxxxxxxxx", only_active=False, page=1, items_per_page=2000)

        print(paging.page_number)
        print(paging.items_per_page)
        print(paging.total_items)

        for notification in paging.items:
            print(notification.created)
            print(notification.alarmNumber)
            print(notification.header)
            print(notification.status)

asyncio.run(main())