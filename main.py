import asyncio
import time
from concurrent import futures

import uvicorn
from fastapi import FastAPI

from core.cpu_bound import blocking_cpu, async_blocking_cpu
from core.io_bound import blocking_io, async_blocking_io
from util.console import print_info

app = FastAPI()
thread_pool = futures.ThreadPoolExecutor(max_workers=10, thread_name_prefix="custom")
process_pool = futures.ProcessPoolExecutor(max_workers=10)


@app.get("/6/async-cpu-bound")
async def async_cpu_bound_6():
    print_info(f"started at {time.strftime('%X')}")
    for i in range(100):
        await asyncio.to_thread(blocking_cpu, 1000)
    print_info(f"finished at {time.strftime('%X')}")

    return {"message": "completed"}


@app.get("/6_1/async-cpu-bound")
async def async_cpu_bound_6_1():
    loop = asyncio.get_event_loop()

    print_info(f"started at {time.strftime('%X')}")
    for i in range(100):
        loop.run_in_executor(thread_pool, blocking_cpu, 1000)

    print_info(f"finished at {time.strftime('%X')}")

    return {"message": "completed"}


@app.get("/6_2/async-cpu-bound")
async def async_cpu_bound_6_2():
    loop = asyncio.get_event_loop()

    print_info(f"started at {time.strftime('%X')}")
    for i in range(100):
        loop.run_in_executor(process_pool, blocking_cpu, 1000)

    print_info(f"finished at {time.strftime('%X')}")

    return {"message": "completed"}


@app.get("/6_3/async-cpu-bound")
async def async_cpu_bound_6_3():
    print_info(f"started at {time.strftime('%X')}")
    for i in range(100):
        await async_blocking_cpu(1000)
    print_info(f"finished at {time.strftime('%X')}")

    return {"message": "completed"}


@app.get("/7/async-io-bound")
async def async_io_bound_7():
    print_info(f"started at {time.strftime('%X')}")
    for i in range(100):
        await asyncio.to_thread(blocking_io)
    print_info(f"finished at {time.strftime('%X')}")

    return {"message": "completed"}


@app.get("/7_1/async-io-bound")
async def async_io_bound_7_1():
    loop = asyncio.get_event_loop()

    print_info(f"started at {time.strftime('%X')}")
    for i in range(100):
        result = await loop.run_in_executor(thread_pool, blocking_io)

    print_info(f"finished at {time.strftime('%X')}")

    return {"message": "completed"}


@app.get("/7_2/async-io-bound")
async def async_io_7bound_7_2():
    loop = asyncio.get_event_loop()

    print_info(f"started at {time.strftime('%X')}")
    for i in range(100):
        await loop.run_in_executor(process_pool, blocking_io)

    print_info(f"finished at {time.strftime('%X')}")

    return {"message": "completed"}


@app.get("/7_3/async-io-bound")
async def async_io_7bound_7_3():
    print_info(f"started at {time.strftime('%X')}")
    for i in range(100):
        await async_blocking_io()
    print_info(f"finished at {time.strftime('%X')}")

    return {"message": "completed"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8282, workers=1)
