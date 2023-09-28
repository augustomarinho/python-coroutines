import asyncio
import time
from concurrent import futures

from core.cpu_bound import block_cpu
from util.console import print_info
from util.measure import measure_performance


def run_async_function():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(block_cpu(1000))


@measure_performance
async def main():
    loop = asyncio.get_running_loop()

    print("Case 6_2")
    print_info(f"started at {time.strftime('%X')}")
    with futures.ProcessPoolExecutor(max_workers=3) as pool:
        for i in range(100000):
            loop.run_in_executor(pool, block_cpu, 1000)
    print_info(f"finished at {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())
