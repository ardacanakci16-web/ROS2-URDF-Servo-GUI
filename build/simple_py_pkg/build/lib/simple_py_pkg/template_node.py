#!/usr/bin/env python3

# 1.library
import rclpy
from rclpy.node import Node

class CustomNodeName(Node):
    def __init__(self):
        super().__init__("custom_node_name")



#2.method
def main(args=None):
    rclpy.init(args=args)
    node = CustomNodeName()
    rclpy.spin(node)
    rclpy.shutdown()


   


if __name__ == "__main__":
    main()