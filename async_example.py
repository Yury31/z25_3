import asyncio
import time
import random

loop = asyncio.get_event_loop()


async def http_request():
    await asyncio.sleep(1)
    return {'res': 'Response'}


async def db_request():
    await asyncio.sleep(1)
    return [1, 2, 3]


async def some_logic():
    # http, db = await asyncio.gather(http_request(), db_request())
    http = await http_request()
    db = await db_request()
    return http, db


start = time.time()
res = loop.run_until_complete(some_logic())
print('END', time.time() - start)
print(res)


async def task(task_id):
    await asyncio.sleep(random.randint(0, 5) * 0.001)
    print('Task done:', task_id)


async def run_tasks(count):
    tasks = [task(i) for i in range(count)]
    await asyncio.wait(tasks)


loop.run_until_complete(run_tasks(10))


class AsyncClassExample:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    async def __aenter__(self):
        await task(1)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def __anext__(self):
        pass

    async def __aiter__(self):
        return self


with AsyncClassExample():
    pass

async with AsyncClassExample():
    pass

async for item in AsyncClassExample():
    print(item)
