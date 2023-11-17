#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_srvs.srv import SetBool

class BoolServiceNode(Node):
    def __init__(self):
        super().__init__("main_server")
        self.service = self.create_service(SetBool, '/set_lift', self.callback)
        self.get_logger().info('Service server is ready to receive requests.')

    def callback(self, request, response):
        # Handle the service request and set the response value
        if request.data:
            # Do something when the request is True
            response.success = True
            response.message = "Request succeeded"
            print("Request succeeded")
        else:
            # Do something when the request is False
            response.success = False
            response.message = "Request failed"
            print("Request failed")

        return response

def main(args=None):
    rclpy.init(args=args)

    node = BoolServiceNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("KeyboardInterrupt, shutting down")

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()