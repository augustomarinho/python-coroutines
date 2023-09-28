import asyncio

from util.console import print_info


async def hello(name: str = "World"):
    print_info(f"Hello {name}")


if __name__ == '__main__':
    asyncio.run(hello())
