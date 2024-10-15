import asyncio
import websockets
import base64
from picamera import PiCamera
from io import BytesIO

# WebSocket server address
WS_SERVER_URI = "ws://your_websocket_server_address"

# Initialize PiCamera
camera = PiCamera()
camera.resolution = (640, 480)  # Set the resolution of the photo


async def capture_and_send_image(websocket):
    """Capture an image using PiCamera and send it to the WebSocket server."""
    # Capture image to an in-memory stream (BytesIO)
    image_stream = BytesIO()
    camera.capture(image_stream, format="jpeg")  # Capture the image in JPEG format
    image_stream.seek(0)  # Move the stream position to the beginning

    # Convert the image to base64 to send it via WebSocket
    image_data = image_stream.read()
    encoded_image = base64.b64encode(image_data).decode("utf-8")

    # Send the image to the server
    await websocket.send(encoded_image)
    print("Image sent to the server.")


async def start_capture(websocket):
    """Start the photo capture process on command."""
    try:
        async for message in websocket:
            if message == "capture":
                print("Capture command received. Taking a photo...")
                await capture_and_send_image(websocket)
            elif message == "stop":
                print("Stop command received. Closing connection.")
                break
    except websockets.exceptions.ConnectionClosed:
        print("Connection to server closed.")
    finally:
        camera.close()  # Close the camera after use


async def main():
    """Connect to WebSocket server and wait for capture commands."""
    async with websockets.connect(WS_SERVER_URI) as websocket:
        await start_capture(websocket)


# Run the WebSocket client
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
