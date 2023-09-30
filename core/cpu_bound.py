# from util.console import print_info


def block_cpu(number):
    """
    Calculate factorial of a number
    :param number:
    :return: factorial of number
    """
    f = 1
    for i in range(2, number + 1):
        f *= i
    # print_info(f"factorial({number}) = {f}")
    return f


async def async_block_cpu(number):
    """
    Calculate factorial of a number
    :param number:
    :return: factorial of number
    """
    f = 1
    for i in range(2, number + 1):
        f *= i
    # print_info(f"factorial({number}) = {f}")
    return f
