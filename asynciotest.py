import asyncio

import aiohttp
import requests


async def sum(x, y):
    asyncio.sleep(2)
    print("sum")
    return x + y


async def get(url):
    res = requests.get(url)
    return res


async def aio_get(url):
    session = aiohttp.ClientSession()
    res = await session.get(url=url)
    text = await res.text()
    session.close()
    return text


async def request(url):
    # res = await get(url)
    res = await aio_get(url)
    # print(res.result())
    return res


def run():
    loop = asyncio.get_event_loop()
    cor = [asyncio.ensure_future(request("http://127.0.0.1:8000/modules/")) for _ in range(5)]
    loop.run_until_complete(asyncio.wait(cor))
    for c in cor:
        print(c.result())


if __name__ == "__main__":
    # for i in range(5):
    # sum(1, 2)
    run()
