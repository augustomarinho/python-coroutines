import asyncio
import time
from concurrent import futures

from core.io_bound import blocking_io
from util.console import print_info
from util.measure import measure_performance


@measure_performance
async def main():
    loop = asyncio.get_running_loop()

    print("Case 7_2")
    print_info(f"started at {time.strftime('%X')}")
    with futures.ProcessPoolExecutor(max_workers=3) as pool:
        for i in range(100):
            loop.run_in_executor(pool, blocking_io)
    print_info(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
