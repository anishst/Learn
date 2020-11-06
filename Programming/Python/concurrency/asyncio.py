#  https://realpython.com/async-io-python/
#https://medium.com/better-programming/every-python-programmer-should-know-the-not-so-secret-threadpool-642ec47f2000

from datetime import datetime
import aiohttp
import asyncio

URL = "https://medium.fabianbosler.de/run"


async def sample_asyncio(samples):
    start = datetime.now()

    async def main():
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as resp:
                return await resp.json()

    results = await asyncio.gather(*[main() for _ in range(samples)])

    return results, datetime.now()-start

if __name__ == '__main__':
    print(asyncio.run(sample_asyncio(64))[1])