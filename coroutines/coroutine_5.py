import asyncio
import time

from util.console import print_info
from util.measure import measure_performance


async def block_cpu(number):
    """
    Calculate factorial of a number
    :param number:
    :return: factorial of number
    """
    f = 1
    for i in range(2, number + 1):
        f *= i
    print_info(f" factorial({number}) = {f}")
    return f


@measure_performance
async def main():
    print_info(f"started at {time.strftime('%X')}")
    result = await asyncio.gather(
        block_cpu(1000),
        block_cpu(1000),
        block_cpu(1000),
    )
    print_info(result)
    print_info(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
