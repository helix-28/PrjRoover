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


        # Créer un message Twist pour la commande
        cmd_vel = Twist()
        cmd_vel.linear.x = gauche_x  # Utilisation de la vitesse linéaire sur l'axe X
        cmd_vel.linear.y = gauche_y
        cmd_vel.angular.z = droite_x
        # Log pour débogage
        self.get_logger().info(f"vx: {cmd_vel.linear.x}, vy: {cmd_vel.linear.y}, Rotation: {cmd_vel.linear.z}")
        # Publier sur le topic cmd_vel
        self.publisher_.publish(cmd_vel)



def main(args=None):
    rclpy.init(args=args)
    node = JoystickToCmdVel()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()



