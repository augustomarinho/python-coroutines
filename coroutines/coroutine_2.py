import asyncio
import time

from util.console import print_info


async def hello(name: str = "World"):
    print_info(f"Hello {name}")
    await asyncio.sleep(1)


async def main():
    print_info(f"started at {time.strftime('%X')}")
    await hello("Augusto")
    await hello("Marinho")
    print_info(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
