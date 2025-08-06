 # Used for non-blocking I/O operations like file reading, API calls,etc.

  # Basic Example

import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())



#  Running Multiple Tasks

async def task(name):
    print(f"{name} started")
    await asyncio.sleep(1)
    print(f"{name} finished")

async def main():
    await asyncio.gather(task("A"), task("B"))

asyncio.run(main())
