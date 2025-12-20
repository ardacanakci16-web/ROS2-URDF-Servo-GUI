#!/usr/bin/env python3

# 1.library
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
class ChannelNode(Node):
    def __init__(self):
        super().__init__("channel_node")
        
        
        
        self.greeting_ = "hİ awesome people :"
        self.publisher_ = self.create_publisher(String, "channel_something", 10)
        self.timer_ = self.create_timer(0.5, self.publish_channel)
        self.get_logger().info("Channel Something has been publisher !")
    
    
    
    
    
    def publish_channel(self):
        msg = String()
        msg.data =str(self.greeting_) + "Welcome to the Channel something"
        self.publisher_.publish(msg)
#2.method
def main(args=None):
    rclpy.init(args=args)
    node =ChannelNode()
    rclpy.spin(node)
    rclpy.shutdown()


   


if __name__ == "__main__":
    main()