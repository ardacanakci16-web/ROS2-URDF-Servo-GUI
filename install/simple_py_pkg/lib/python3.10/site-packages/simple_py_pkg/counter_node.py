#!/usr/bin/env python3

# 1.library
import rclpy
from rclpy.node import Node

class CounterNode(Node):
    def __init__(self):
        super().__init__("counter_node")
        self.counter_ = 0
        self.create_timer(0.5 ,self.timer_callback)
        

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello World! - "+str(self.counter_))    




def main(args=None):
    rclpy.init(args=args)
    node = CounterNode()
    rclpy.spin(node)
    rclpy.shutdown()


   


if __name__ == "__main__":
    main()