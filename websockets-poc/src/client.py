import asyncio
import websockets
import itertools

URI = "ws://localhost:8765"


async def main():
    counter = itertools.count()

    try:
        async with websockets.connect(URI) as websocket:
            print("Connected to server")

            while True:
                i = next(counter)
                message = f"message {i}"
                print(f"Sending: {message}")

                await websocket.send(message)
                response = await websocket.recv()
                print(f"Received: {response}")

                await asyncio.sleep(1)  # throttle messages
    except KeyboardInterrupt:
        print("Client interrupted, exiting...")
    except Exception as e:
        print(f"Client error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
