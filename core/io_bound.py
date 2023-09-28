import time

from util.console import print_info


def blocking_io():
    with open('/dev/urandom', 'rb') as f:
        for _ in range(1000):
            result = int.from_bytes(f.read(1000), 'big')
            print_info(f"value readed: {result}")
