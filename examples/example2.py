import asyncio
import aiohttp

from myuplink.auth import Auth
from myuplink.api import MyUplinkAPI


async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, "https://api.myuplink.com", "eyJhbGciOiJSUzI1NiIsImtpZCI6IkI3NDEwMDI3NjJGQ0MzOTQ3OTA1RTA0QUIxREFBMjNGMjk4MzIzQ0ZSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InQwRUFKMkw4dzVSNUJlQktzZHFpUHltREk4OCJ9.eyJuYmYiOjE3MDc3MzM2MzQsImV4cCI6MTcwNzczNzIzNCwiaXNzIjoiaHR0cHM6Ly9hcGkubXl1cGxpbmsuY29tIiwiYXVkIjoiQVBJLXYyIiwiY2xpZW50X2lkIjoiYjdkODc0ZjYtZmM4Yi00NDkyLWFmODAtYjJhYTY2MTMxYzEwIiwic3ViIjoiNjRkMWQ1YzMtOTJjMS00NjNkLTdjMWYtMDhkYTAxOGE1NTQ2IiwiYXV0aF90aW1lIjoxNzA3NzI5MjYxLCJpZHAiOiJsb2NhbCIsImlzZGVtbyI6IkZhbHNlIiwidW5pdHN5c3RlbSI6Ik1ldHJpYyIsImp0aSI6IkMzODQ2RUE1NDlFMzNENjUwNkY5Q0JDNkU4RUE5OUY3Iiwic2lkIjoiRTZCNUYzMUUzQUUyQkU3MzZERDY0QTgyNERFQ0VDQkEiLCJpYXQiOjE3MDc3MzM2MzQsInNjb3BlIjpbIlJFQURTWVNURU0iLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsicHdkIl19.v2qmCSe_UtxaVi81u5UmX3eiGSJkuw97v8zvYj-j_AjDO5rBYiSaxKf9RjTn9OmYVSWQ9QkVBKOLdV8FYNazUDLnm5W20JLRSkX0tKv6m2vkrczX0PKp2zsvemjj2PslRFGUtV3_2M8BTdTofeexER5f9Esr1nTQsxHBSBd4zN6foR-WsAxYgKNpKqLm5k1W3NAbvHZm7UBFHKDZEr40N5bh2mtFCzWuk9YEUxq03rdsEsRTjuHxQaXWVgb4JivjppKg5oAWrq4wszXprIVM8WCU_GgIdC64LIEPC-EvTdwopTv_TFJg7IZaDy0rQ2MCmosfb04bKTe8zQwpXZFLHQ")
        api = MyUplinkAPI(auth)

        paging = await api.async_get_system_notifications(system_id="1869957b-92c3-4dfd-b961-f113d53eb44d", only_active=False, page=1, items_per_page=2000)

        print(paging.page_number)
        print(paging.items_per_page)
        print(paging.total_items)

        for notification in paging.items:
            print(notification.created)
            print(notification.alarmNumber)
            print(notification.header)
            print(notification.status)

asyncio.run(main())