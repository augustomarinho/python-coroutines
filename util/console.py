import asyncio
import inspect
import threading


def print_info(*args):
    if inspect.iscoroutinefunction(print_info):
        print(f"[native_id={threading.get_native_id()} "
              f"ident={threading.get_ident()} "
              f"task_name={asyncio.current_task(): asyncio.current_task().get_coro().__qualname__} "
              f"task_id={id(asyncio.current_task().get_coro())}] ",
              *args,
              sep='',
              end="\n",
              flush=False
              )
    else:
        print(f"[native_id={threading.get_native_id()} "
              f"ident={threading.get_ident()}] ",
              *args,
              sep='',
              end="\n",
              flush=False
              )
