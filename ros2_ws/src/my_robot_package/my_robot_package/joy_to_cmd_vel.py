import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pygame
import math

class JoystickToCmdVel(Node):
    def __init__(self):
        super().__init__('joy_to_cmd_vel')

        # Initialisation du publisher ROS 2
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        # Initialisation de pygame pour lire la manette
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            self.get_logger().error("Aucune manette détectée.")
            return

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.get_logger().info(f"Manette détectée: {self.joystick.get_name()}")

        # Boucle principale
        self.timer = self.create_timer(0.1, self.timer_callback)  # Publie toutes les 100ms

    def timer_callback(self):
        # Récupérer les données de la manette
        pygame.event.pump()

        gauche_x = self.joystick.get_axis(0)  # joystick gauche horizontal (X)
        gauche_y = self.joystick.get_axis(1)  # joystick gauche vertical (Y)
        droite_x = self.joystick.get_axis(3)  # joystick droit horizontal (X)

        # Calcul de la vitesse et de l'angle
        vitesse = math.sqrt(gauche_x**2 + gauche_y**2)  # échelle entre 0 et 1
        vitesse = min(vitesse, 1.0)  # Limiter la vitesse à 1.0
        angle = math.degrees(math.atan2(gauche_y, gauche_x))  # calcul de l'angle
        rotation = droite_x  # rotation gauche/droite sur joystick droit

        # Créer un message Twist pour la commande
        cmd_vel = Twist()
        cmd_vel.linear.x = vitesse * 1.0  # vitesse linéaire (scale entre -1.0 et 1.0)
        cmd_vel.angular.z = rotation * 1.0  # rotation angulaire (scale entre -1.0 et 1.0)

        # Publier sur le topic cmd_vel
        self.publisher_.publish(cmd_vel)

        # Log pour débogage
        self.get_logger().info(f"Vitesse: {vitesse}, Angle: {angle}, Rotation: {rotation}")


def main(args=None):
    rclpy.init(args=args)
    node = JoystickToCmdVel()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



