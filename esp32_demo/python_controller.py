import pygame
import websockets
import asyncio

# Initialize pygame
pygame.init()

# Initialize the joystick (Xbox controller)
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Connect to ESP32 WebSocket server (use ESP32's IP address in the same network)
esp32_ip = "172.20.10.5"  # Replace with the IP address of your ESP32
port = 81  # The port on which ESP32 listens
url = f"ws://{esp32_ip}:{port}"

# Create a WebSocket client connection
async def send_data():
    async with websockets.connect(url) as websocket:
        while True:
            # Get joystick input
            pygame.event.pump()
            x_axis = joystick.get_axis(0)  # Left-right axis
            y_axis = joystick.get_axis(1)  # Up-down axis
            button_a = joystick.get_button(0)  # Button A (1 if pressed, 0 if not)

            # Prepare message
            message = f"{x_axis},{y_axis},{button_a}"

            # Send joystick data to ESP32
            await websocket.send(message)
            
            # Receive obstacle data from ESP32
            obstacle_data = await websocket.recv()
            print(f"Obstacle Data: {obstacle_data}")

            await asyncio.sleep(0.1)  # Control loop speed

# Start the asyncio loop
asyncio.get_event_loop().run_until_complete(send_data())
