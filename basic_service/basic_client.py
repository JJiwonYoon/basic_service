#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_srvs.srv import SetBool

class BoolClientNode(Node):
    def __init__(self):
        super().__init__("main_client")
        self.client = self.create_client(SetBool, '/set_lift')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')

    def send_request(self, data):
        request = SetBool.Request()
        request.data = data

        # Call the service
        future = self.client.call_async(request)

        # Wait for the result (timeout set to 1 second for simplicity)
        rclpy.spin_until_future_complete(self, future, timeout_sec=1.0)

        # Check if the service call was successful
        if future.result() is not None:
            response = future.result()
            self.get_logger().info('Service call successful. Success: %s, Message: %s' % (response.success, response.message))
        else:
            self.get_logger().warning('Service call failed')

def main(args=None):
    rclpy.init(args=args)

    client_node = BoolClientNode()

    try:
        # Call the service with a boolean value
        client_node.send_request(True)
    except KeyboardInterrupt:
        print("KeyboardInterrupt, shutting down")

    client_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()