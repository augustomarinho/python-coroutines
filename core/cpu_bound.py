
def blocking_cpu(number):
    """
    Calculate factorial of a number
    :param number:
    :return: factorial of number
    """
    f = 1
    for i in range(2, number + 1):
        f *= i
    return f


async def async_blocking_cpu(number):
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
