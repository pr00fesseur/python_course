# async/await
import asyncio


async def foo():
    await asyncio.sleep(1)
    print("I am foo")


async def bar():
    await asyncio.sleep(2)
    print("I am bar")


async def main():
    tasks = [foo(), bar()]
    results = await asyncio.gather(*tasks)
    # await foo()
    # await bar()


if __name__ == "__main__":
    asyncio.run(main())
    # main()
    # print(foo())
    # print(main())
