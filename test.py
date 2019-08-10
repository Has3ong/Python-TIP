import asyncio
import aiohttp
import time

loop = asyncio.get_event_loop()

async def hello(URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            response = await response.read()
            print(response)
            print(time.time())

loop.run_until_complete(asyncio.wait([
    hello("http://httpbin.org/headers"),
    hello("http://httpbin.org/headers")
]))