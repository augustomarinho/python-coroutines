import asyncio
import time

from util.console import print_info
from util.measure import measure_performance


async def hello(name: str = "World"):
    print_info(f"Hello {name}")
    await asyncio.sleep(1)


@measure_performance
async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(
            hello("Augusto"))
        tg.create_task(
            hello("Marinho"))
        print_info(f"started at {time.strftime('%X')}")

    print_info(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
