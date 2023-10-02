import asyncio
import time

from core.cpu_bound import async_blocking_cpu
from util.console import print_info
from util.measure import measure_performance


@measure_performance
async def main():
    print("Case 6_3")
    print_info(f"started at {time.strftime('%X')}")
    for i in range(100000):
        await async_blocking_cpu(1000)
    print_info(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
