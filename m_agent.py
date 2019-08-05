import asyncio
from aiohttp import ClientSession
from req import RequestBuilder, RequestBuilderEncoder


class Agent:
    def __init__(self, L):
        self.L = L

    async def validate(self, url, session):

        # valid request
        r = RequestBuilder()
        valid_req = RequestBuilderEncoder().encode(r)
        async with session.post(url, data=valid_req, headers={'content-type': 'application/json'}) as response:
            self.L.append(response.status)
            return await response.read()

    async def run(self, r):
        url = "http://localhost:5000/validate_request"
        tasks = []

        async with ClientSession() as session:
            count = 0
            for i in range(r):
                task = asyncio.ensure_future(self.validate(url, session))
                tasks.append(task)
                count += 1

            await asyncio.gather(*tasks)

    def ex(self, num=10):
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self.run(num))
        loop.run_until_complete(future)

