import asyncio
import time
from concurrent import futures

import uvicorn
from fastapi import FastAPI

from core.cpu_bound import block_cpu
from core.io_bound import blocking_io
from util.console import print_info
from util.measure import measure_performance

app = FastAPI()


@app.get("/6/async-cpu-bound")
async def async_cpu_bound_6():
    @measure_performance
    async def inner():
        print_info(f"started at {time.strftime('%X')}")
        for i in range(100000):
            print_info(f"loop {i}")
            await asyncio.to_thread(block_cpu, 1000)
        print_info(f"finished at {time.strftime('%X')}")

    await inner()
    return {"message": "completed"}


@app.get("/6_1/async-cpu-bound")
async def async_cpu_bound_6_1():
    @measure_performance
    async def inner():
        loop = asyncio.get_running_loop()

        print_info(f"started at {time.strftime('%X')}")
        with futures.ThreadPoolExecutor(max_workers=3,
                                        thread_name_prefix="custom") as pool:
            for i in range(100000):
                print_info(f"loop {i}")
                loop.run_in_executor(pool, block_cpu, 1000)
        print_info(f"finished at {time.strftime('%X')}")

    await inner()

    return {"message": "completed"}


@app.get("/6_2/async-cpu-bound")
async def async_cpu_bound_6_2():
    @measure_performance
    async def inner():
        loop = asyncio.get_running_loop()

        print_info(f"started at {time.strftime('%X')}")
        with futures.ProcessPoolExecutor(max_workers=3) as pool:
            for i in range(100000):
                print_info(f"loop {i}")
                loop.run_in_executor(pool, block_cpu, 1000)
        print_info(f"finished at {time.strftime('%X')}")

    await inner()

    return {"message": "completed"}


@app.get("/7/async-io-bound")
async def async_io_bound_7():
    @measure_performance
    async def inner():
        print_info(f"started at {time.strftime('%X')}")
        for i in range(100):
             # print_info(f"loop {i}")
            await asyncio.to_thread(blocking_io)
        print_info(f"finished at {time.strftime('%X')}")

    await inner()

    return {"message": "completed"}

@app.get("/7_1/async-io-bound")
async def async_io_bound_7_1():
    @measure_performance
    async def inner():
        loop = asyncio.get_running_loop()

        print_info(f"started at {time.strftime('%X')}")
        with futures.ThreadPoolExecutor(max_workers=3,
                                        thread_name_prefix="custom") as pool:
            for i in range(100):
                # print_info(f"loop {i}")
                loop.run_in_executor(pool, blocking_io)
        print_info(f"finished at {time.strftime('%X')}")

    await inner()

    return {"message": "completed"}


@app.get("/7_2/async-io-bound")
async def async_io_7bound_7_2():
    @measure_performance
    async def inner():
        loop = asyncio.get_running_loop()

        print_info(f"started at {time.strftime('%X')}")
        with futures.ProcessPoolExecutor(max_workers=3) as pool:
            for i in range(100):
                # print_info(f"loop {i}")
                loop.run_in_executor(pool, blocking_io)
        print_info(f"finished at {time.strftime('%X')}")

    await inner()

    return {"message": "completed"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8282, workers=1)
