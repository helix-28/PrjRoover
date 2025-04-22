import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import tf2_ros
from geometry_msgs.msg import TransformStamped
import math
from tf_transformations import euler_from_quaternion, quaternion_from_euler


class OdomPublisher(Node):
    def __init__(self):
        super().__init__('odom_publisher')

        # Initial position and orientation (pose of the robot)
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        # ROS2 publisher for the cmd_vel topic
        self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)

        # TF2 broadcaster to publish the dynamic transform
        self.broadcaster = tf2_ros.TransformBroadcaster(self)

        # Timer to update the TF at a regular interval
        self.timer = self.create_timer(0.1, self.publish_transform)  # Update every 100ms

    def cmd_vel_callback(self, msg):
        """Handle incoming cmd_vel messages."""
        # Get linear and angular velocities from cmd_vel
        v = msg.linear.x
        w = msg.angular.z

        # Assuming we use a simple kinematic model with constant time step
        dt = 0.1  # time step for update (100ms)
        
        # Compute the change in position and orientation
        delta_x = v * dt * math.cos(self.theta)
        delta_y = v * dt * math.sin(self.theta)
        delta_theta = w * dt
        
        # Update the robot's position and orientation
        self.x += delta_x
        self.y += delta_y
        self.theta += delta_theta

    def publish_transform(self):
        """Publish the odometry transform to tf."""
        # Create the transform message
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'  # parent frame
        t.child_frame_id = 'base_link'  # child frame

        # Fill in the position and orientation
        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.translation.z = 0.0

        # Convert orientation (theta) to quaternion
        quat = quaternion_from_euler(0.0, 0.0, self.theta)
        t.transform.rotation.x = quat[0]
        t.transform.rotation.y = quat[1]
        t.transform.rotation.z = quat[2]
        t.transform.rotation.w = quat[3]

        # Send the transform
        self.broadcaster.sendTransform(t)


def main(args=None):
    rclpy.init(args=args)
    node = OdomPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
