import asyncio
import time

from core.io_bound import blocking_io
from util.console import print_info
from util.measure import measure_performance


@measure_performance
async def main():
    print_info(f"started at {time.strftime('%X')}")
    for i in range(100):
        print_info(f"loop {i}")
        await asyncio.to_thread(blocking_io)
    print_info(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
