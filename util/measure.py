import inspect

import psutil
import time


def measure_performance(func):
    async def async_wrapper(*args, **kwargs):
        # Start measuring CPU time
        start_time = time.process_time()

        # Get CPU and memory usage before running the function
        cpu_before = psutil.cpu_percent(interval=None)
        memory_before = psutil.virtual_memory().percent

        # Execute the wrapped synchronous function
        result = await func(*args, **kwargs)

        # Measure CPU time
        cpu_time = time.process_time() - start_time

        # Get CPU and memory usage after running the function
        cpu_after = psutil.cpu_percent(interval=None)
        memory_after = psutil.virtual_memory().percent

        # Calculate CPU and memory usage differences
        cpu_usage = cpu_after - cpu_before
        memory_usage = memory_after - memory_before

        print("-" * 50)
        print(f"Function '{func.__name__}' Metrics (Async):")
        print(f"CPU Occupation: {cpu_usage:.2f}%")
        print(f"Memory Occupation: {memory_usage:.2f}%")
        print(f"CPU Time: {cpu_time:.4f} seconds")
        print("-" * 50)

        return result

    def sync_wrapper(*args, **kwargs):
        # Start measuring CPU time
        start_time = time.process_time()

        # Get CPU and memory usage before running the function
        cpu_before = psutil.cpu_percent(interval=None)
        memory_before = psutil.virtual_memory().percent

        # Execute the wrapped synchronous function
        result = func(*args, **kwargs)

        # Measure CPU time
        cpu_time = time.process_time() - start_time

        # Get CPU and memory usage after running the function
        cpu_after = psutil.cpu_percent(interval=None)
        memory_after = psutil.virtual_memory().percent

        # Calculate CPU and memory usage differences
        cpu_usage = cpu_after - cpu_before
        memory_usage = memory_after - memory_before

        print("-"*50)
        print(f"Function '{func.__name__}' Metrics (Sync):")
        print(f"CPU Occupation: {cpu_usage:.2f}%")
        print(f"Memory Occupation: {memory_usage:.2f}%")
        print(f"CPU Time: {cpu_time:.4f} seconds")
        print("-" * 50)

        return result

    if inspect.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper
