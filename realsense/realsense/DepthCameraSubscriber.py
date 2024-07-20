import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class DepthCameraSubscriber(Node):
    def __init__(self):
        super().__init__('realsense_depth')
        self.subscription = self.create_subscription(
            Image,
            'camera/depth/image_raw',
            self.image_callback,
            10)
        self.bridge = CvBridge()

    def image_callback(self, msg):
        # cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='32FC1')
        # cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='16UC1')
        cv2.imshow('Depth Camera Image', cv_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = DepthCameraSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
