# TODO remove this when client is modified to communicate with stateful server

import asyncio

from websockets.asyncio.client import connect


async def hello():
    uri = "ws://localhost:8765"
    async with connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")
