import asyncio
import time
from concurrent import futures

import uvicorn
from fastapi import FastAPI

from core.cpu_bound import block_cpu, block_cpu_sync
from util.console import print_info
from util.measure import measure_performance

app = FastAPI()



@app.get("/6/async-cpu-bound")
async def async_cpu_bound():
    @measure_performance
    async def inner():
        print_info(f"started at {time.strftime('%X')}")
        for i in range(100000):
            await block_cpu(1000)
        print_info(f"finished at {time.strftime('%X')}")

    await inner()
    return {"message": "completed"}


@measure_performance
@app.get("/6_1/async-cpu-bound")
async def async_cpu_bound():
    loop = asyncio.get_running_loop()

    print_info(f"started at {time.strftime('%X')}")
    with futures.ThreadPoolExecutor(max_workers=10,
                                    thread_name_prefix="999") as pool:
        for i in range(100000):
            print_info(f"loop {i}")
            loop.run_in_executor(pool, block_cpu_sync, 1000)
    print_info(f"finished at {time.strftime('%X')}")

    return {"message": "completed"}


@measure_performance
@app.get("/6_2/async-cpu-bound")
async def async_cpu_bound():
    loop = asyncio.get_running_loop()

    print_info(f"started at {time.strftime('%X')}")
    with futures.ProcessPoolExecutor(max_workers=10) as pool:
        for i in range(100000):
            print_info(f"loop {i}")
            await loop.run_in_executor(pool, block_cpu_sync, 1000)
    print_info(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8282, workers=1)
