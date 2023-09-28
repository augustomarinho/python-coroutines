import time

from util.console import print_info


def blocking_io():
    print_info(f"started block at {time.strftime('%X')}")
    with open('/dev/urandom', 'rb') as f:
        for _ in range(1000):
            print_info(f"value readed {int.from_bytes(f.read(1000), 'big')}")
    print_info(f"finished block at {time.strftime('%X')}")
