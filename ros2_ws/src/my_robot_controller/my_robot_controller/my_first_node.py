#! /usr/bin/env python3


import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")
        self.create_timer(1.0, self.timer_callback)


    def timer_callback(self):
        self.get_logger().info("Hello")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node) # it can keep the node alive in an infinitive loop until we kill it in the terminal 
    rclpy.shutdown()
if __name__ == '__main__':
    main()



