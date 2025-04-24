import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster

class OdometryPublisher(Node):

    def __init__(self):
        super().__init__('odom_publisher')
        self.odom_pub = self.create_publisher(Odometry, 'odom', 10)
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.publish_odom)

    def publish_odom(self):
        # Créer un message d'odométrie
        odom_msg = Odometry()
        # Remplir les détails de l'odom_msg ici
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = "odom"
        odom_msg.child_frame_id = "base_link"

        # Publier le message d'odométrie
        self.odom_pub.publish(odom_msg)

        # Créer un message de transformation
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = "odom"
        transform.child_frame_id = "base_link"

        # Définir les valeurs de translation et de rotation
        transform.transform.translation.x = 0.0  # Remplacer par les valeurs réelles
        transform.transform.translation.y = 0.0  # Remplacer par les valeurs réelles
        transform.transform.translation.z = 0.0  # Remplacer par les valeurs réelles

        transform.transform.rotation.x = 0.0  # Remplacer par les valeurs réelles
        transform.transform.rotation.y = 0.0  # Remplacer par les valeurs réelles
        transform.transform.rotation.z = 0.0  # Remplacer par les valeurs réelles
        transform.transform.rotation.w = 1.0  # Remplacer par les valeurs réelles

        # Publier la transformation
        self.tf_broadcaster.sendTransform(transform)

def main(args=None):
    rclpy.init(args=args)
    node = OdometryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

