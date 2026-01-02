import asyncio
import json
import random
import uuid
from datetime import datetime

import websockets

URI = "ws://localhost:8765"
CLIENT_ID = str(uuid.uuid4())

async def main():
    async with websockets.connect(URI) as websocket:
        print(f"Client {CLIENT_ID} connected")

        publish_count = random.randint(1, 10)
        print(f"Publishing {publish_count} initial messages")

        for i in range(publish_count):
            message = {
                "client_id": CLIENT_ID,
                "message_index": i,
                "total_messages": publish_count,
                "timestamp": datetime.utcnow().isoformat(),
            }

            await websocket.send(json.dumps(message))
            print(f"Sent: {message}")

            await asyncio.sleep(0.2)

        print("Initial publish completed. Switching to receive-only mode.")

        async for message in websocket:
            data = json.loads(message)
            print(f"Received broadcast: {data}")


if __name__ == "__main__":
    asyncio.run(main())
