import asyncio
import json
from datetime import datetime
from typing import Set

import websockets
from websockets.server import ServerConnection

HOST = "localhost"
PORT = 8765

connected_clients: Set[ServerConnection] = set()


async def broadcast(message: dict):
    if not connected_clients:
        return

    payload = json.dumps(message)
    await asyncio.gather(
        *(client.send(payload) for client in connected_clients),
        return_exceptions=True
    )


async def handler(websocket: ServerConnection):
    connected_clients.add(websocket)
    client_id = id(websocket)

    print(f"Client connected: {client_id}")

    try:
        async for raw_message in websocket:
            data = json.loads(raw_message)

            event = {
                "type": "broadcast",
                "from": client_id,
                "timestamp": datetime.utcnow().isoformat(),
                "payload": data,
            }

            print(f"Broadcasting from {client_id}")
            await broadcast(event)

    except websockets.ConnectionClosed:
        print(f"Client disconnected: {client_id}")
    finally:
        connected_clients.discard(websocket)


async def main():
    print(f"Broadcast WebSocket server running on ws://{HOST}:{PORT}")
    async with websockets.serve(handler, HOST, PORT):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
