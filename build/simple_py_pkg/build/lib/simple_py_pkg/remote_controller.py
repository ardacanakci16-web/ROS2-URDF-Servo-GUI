#!/usr/bin/env python3

# 1.library
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RemoteControllerNode(Node):
    def __init__(self):
        super().__init__("remote_controller_node")
        self.subscriber_ = self.create_subscription(String, "channel_something",
                                                    self.callback_television, 10)

        self.get_logger().info("Remote_Controller has been subscried !")


    def callback_television(self,msg):
        self.get_logger().info(msg.data)


#2.method
def main(args=None):
    rclpy.init(args=args)
    node = RemoteControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()


   


if __name__ == "__main__":
    main()