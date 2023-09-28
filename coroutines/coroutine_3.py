import asyncio
import time

from util.console import print_info


async def hello(name: str = "World"):
    print_info(f"Hello {name}")
    await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(
        hello("Augusto"))
    task2 = asyncio.create_task(
        hello("Marinho"))

    print_info(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print_info(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
