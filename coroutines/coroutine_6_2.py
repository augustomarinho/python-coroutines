import asyncio
import time
from concurrent import futures

from core.cpu_bound import block_cpu_sync, block_cpu
from util.console import print_info
from util.measure import measure_performance


def run_async_function():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(block_cpu(1000))


@measure_performance
async def main():

    print_info(f"started at {time.strftime('%X')}")
    with futures.ProcessPoolExecutor(max_workers=1) as pool:
        for i in range(100000):
            print_info(f"loop {i}")
            pool.submit(run_async_function)
    print_info(f"finished at {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())
