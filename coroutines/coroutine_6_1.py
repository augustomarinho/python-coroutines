import asyncio
import time
from concurrent import futures

from core.cpu_bound import block_cpu
from util.console import print_info
from util.measure import measure_performance


def run_async_function(loop):
    loop.run_until_complete(block_cpu(1000))


@measure_performance
async def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    print("Case 6_1")
    print_info(f"started at {time.strftime('%X')}")
    with futures.ThreadPoolExecutor(max_workers=3,
                                    thread_name_prefix="custom") as pool:
        for i in range(100000):
            loop.run_in_executor(pool, block_cpu, 1000)

    loop.close()
    print_info(f"finished at {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())
