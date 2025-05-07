import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
import numpy as np
from PIL import Image
import base64
import asyncio
import websockets
import threading
import io

class MapWebSocketNode(Node):
    def __init__(self):
        super().__init__('map_websocket_node')
        self.subscription = self.create_subscription(
            OccupancyGrid,
            'map',
            self.map_callback,
            10)
        self.map_data = None
        self.clients = set()
        threading.Thread(target=self.run_websocket_server, daemon=True).start()

    def map_callback(self, msg):
        self.get_logger().info('Carte reçue')
        width = msg.info.width
        height = msg.info.height
        data = np.array(msg.data, dtype=np.int8).reshape((height, width))

        # Convert map to grayscale image
        img_array = np.zeros((height, width), dtype=np.uint8)
        img_array[data == 0] = 255      # Free space
        img_array[data == 100] = 0      # Occupied
        img_array[data == -1] = 127     # Unknown

        img = Image.fromarray(img_array, mode='L').transpose(Image.FLIP_TOP_BOTTOM)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        img_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')

        asyncio.run(self.broadcast(img_b64))

    async def broadcast(self, img_data):
        if self.clients:
            message = f'data:image/png;base64,{img_data}'
            await asyncio.wait([client.send(message) for client in self.clients])

    async def handler(self, websocket, path):
        self.clients.add(websocket)
        try:
            await websocket.wait_closed()
        finally:
            self.clients.remove(websocket)

    def run_websocket_server(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        start_server = websockets.serve(self.handler, "0.0.0.0", 8765)
        loop.run_until_complete(start_server)
        loop.run_forever()

def main(args=None):
    rclpy.init(args=args)
    node = MapWebSocketNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()