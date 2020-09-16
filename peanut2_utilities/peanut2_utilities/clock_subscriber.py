import rclpy
from rclpy.node import Node

from rosgraph_msgs.msg import Clock

class ClockSubscriber(Node):

    def __init__(self):
        super().__init__('clock_subscriber')
        self.subscription = self.create_subscription( Clock, '/clock', self.listener_callback, 1)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        pass

def main(args=None):
    rclpy.init(args=args)

    clock_subscriber = ClockSubscriber()
    rclpy.spin(clock_subscriber)
    
    clock_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
