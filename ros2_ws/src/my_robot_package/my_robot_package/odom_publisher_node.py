import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped, Twist
from tf2_ros import TransformBroadcaster
from tf_transformations import quaternion_from_euler
import math

class OdometryPublisher(Node):

    def __init__(self):
        super().__init__('odom_publisher')
        self.odom_pub = self.create_publisher(Odometry, 'odom', 10)
        self.tf_broadcaster = TransformBroadcaster(self)

        # Souscription au topic cmd_vel pour récupérer les commandes de mouvement
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10
        )

    def cmd_vel_callback(self, msg):
        self.publish_odom(msg)

    def publish_odom(self, msg):
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = "odom"
        odom_msg.child_frame_id = "base_link"

        vx = msg.linear.x * 10
        vy = msg.linear.y * 10
        rot = msg.angular.z * 10

        # Remplir l'odométrie avec les vitesses linéaires et angulaires
        odom_msg.twist.twist.linear.x = vx
        odom_msg.twist.twist.linear.y = vy
        odom_msg.twist.twist.angular.z = rot

        # Publier l'odométrie
        self.odom_pub.publish(odom_msg)

        # Création du message de transformation
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = "odom"
        transform.child_frame_id = "base_link"

        # Définir les coordonnées x, y
        transform.transform.translation.x = vx
        transform.transform.translation.y = vy
        transform.transform.translation.z = 0.0  # Pas de mouvement vertical

        # Convertir l'angle de rotation Z (yaw) en quaternion
       # qx, qy, qz, qw = self.yaw_to_quaternion(msg.angular.z)
        #transform.transform.rotation.x = qx
        #transform.transform.rotation.y = qy
       # transform.transform.rotation.z = qz
       # transform.transform.rotation.w = qw

        transform.transform.rotation.z = rot


        # Publier la transformation
        self.tf_broadcaster.sendTransform(transform)

    def yaw_to_quaternion(self, yaw):
        # Conversion de yaw (rotation autour de Z) en quaternion
        qz = math.sin(yaw / 2.0)
        qw = math.cos(yaw / 2.0)
        return (0.0, 0.0, qz, qw)

def main(args=None):
    rclpy.init(args=args)
    node = OdometryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
