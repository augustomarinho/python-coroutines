# from util.console import print_info

def blocking_io():
    with open('/dev/urandom', 'rb') as f:
        for _ in range(100):
            result = int.from_bytes(f.read(1000), 'big')
            # print_info(f"value readed: {result}")


async def async_blocking_io():
    with open('/dev/urandom', 'rb') as f:
        for _ in range(10):
            result = int.from_bytes(f.read(1000), 'big')
            # print_info(f"value readed: {result}")
