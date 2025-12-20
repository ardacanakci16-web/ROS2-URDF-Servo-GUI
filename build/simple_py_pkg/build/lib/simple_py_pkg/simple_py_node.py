#!/usr/bin/env python3

# 1.library
import rclpy
from rclpy.node import Node



#2.method
def main(args=None):
    rclpy.init(args=args)
    node = Node("py_node") 


    #print("Hello World!")
    node.get_logger().info("Hello World!")

    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()