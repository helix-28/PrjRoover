import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pygame
import math
import RPi.GPIO as GPIO  # Assure-toi que cette bibliothèque est disponible pour utiliser GPIO

# Définir les broches pour les moteurs (à adapter en fonction de ta configuration)
moteurF_AVNT_DRT = 17
moteurR_AVNT_DRT = 27
moteurF_AVNT_GCH = 22
moteurR_AVNT_GCH = 23
moteurF_ARR_DRT = 24
moteurR_ARR_DRT = 25
moteurF_ARR_GCH = 5
moteurR_ARR_GCH = 6

# Setup des GPIO pour les moteurs
GPIO.setmode(GPIO.BCM)
GPIO.setup(moteurF_AVNT_DRT, GPIO.OUT)
GPIO.setup(moteurR_AVNT_DRT, GPIO.OUT)
GPIO.setup(moteurF_AVNT_GCH, GPIO.OUT)
GPIO.setup(moteurR_AVNT_GCH, GPIO.OUT)
GPIO.setup(moteurF_ARR_DRT, GPIO.OUT)
GPIO.setup(moteurR_ARR_DRT, GPIO.OUT)
GPIO.setup(moteurF_ARR_GCH, GPIO.OUT)
GPIO.setup(moteurR_ARR_GCH, GPIO.OUT)

# Setup des PWM pour les moteurs
p1 = GPIO.PWM(moteurF_AVNT_DRT, 100)
p2 = GPIO.PWM(moteurF_AVNT_GCH, 100)
p3 = GPIO.PWM(moteurF_ARR_GCH, 100)
p4 = GPIO.PWM(moteurF_ARR_DRT, 100)

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)


def direction_mecanum(vitesse, angle, rotation):
    vx = vitesse * math.cos(math.radians(angle))
    vy = vitesse * math.sin(math.radians(angle))

    v_AVNT_DRT = vx + vy + rotation
    v_AVNT_GCH = vx - vy - rotation
    v_ARR_DRT = vx - vy + rotation
    v_ARR_GCH = vx + vy - rotation

    maximum = max(abs(v_AVNT_DRT), abs(v_AVNT_GCH), abs(v_ARR_GCH), abs(v_ARR_DRT))

    if maximum > 100:
        v_ARR_DRT = v_ARR_DRT / maximum * 100
        v_ARR_GCH = v_ARR_GCH / maximum * 100
        v_AVNT_DRT = v_AVNT_DRT / maximum * 100
        v_AVNT_GCH = v_AVNT_GCH / maximum * 100

    # Commande pour chaque roue (avant/droite, avant/gauche, arrière/droite, arrière/gauche)
    if v_AVNT_DRT > 0:
        GPIO.output(moteurF_AVNT_DRT, GPIO.HIGH)
        GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)
    elif v_AVNT_DRT < 0:
        GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)
        GPIO.output(moteurR_AVNT_DRT, GPIO.HIGH)
    else:
        GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)
        GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)

    p1.ChangeDutyCycle(abs(v_AVNT_DRT))

    if v_AVNT_GCH > 0:
        GPIO.output(moteurF_AVNT_GCH, GPIO.HIGH)
        GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)
    elif v_AVNT_GCH < 0:
        GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)
        GPIO.output(moteurR_AVNT_GCH, GPIO.HIGH)
    else:
        GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)
        GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)

    p2.ChangeDutyCycle(abs(v_AVNT_GCH))

    if v_ARR_DRT > 0:
        GPIO.output(moteurF_ARR_DRT, GPIO.HIGH)
        GPIO.output(moteurR_ARR_DRT, GPIO.LOW)
    elif v_ARR_DRT < 0:
        GPIO.output(moteurF_ARR_DRT, GPIO.LOW)
        GPIO.output(moteurR_ARR_DRT, GPIO.HIGH)
    else:
        GPIO.output(moteurF_ARR_DRT, GPIO.LOW)
        GPIO.output(moteurR_ARR_DRT, GPIO.LOW)

    p4.ChangeDutyCycle(abs(v_ARR_DRT))

    if v_ARR_GCH > 0:
        GPIO.output(moteurF_ARR_GCH, GPIO.HIGH)
        GPIO.output(moteurR_ARR_GCH, GPIO.LOW)
    elif v_ARR_GCH < 0:
        GPIO.output(moteurF_ARR_GCH, GPIO.LOW)
        GPIO.output(moteurR_ARR_GCH, GPIO.HIGH)
    else:
        GPIO.output(moteurF_ARR_GCH, GPIO.LOW)
        GPIO.output(moteurR_ARR_GCH, GPIO.LOW)

    p3.ChangeDutyCycle(abs(v_ARR_GCH))


class JoystickToCmdVel(Node):
    def __init__(self):
        super().__init__('joy_to_cmd_vel')

        # Initialisation de pygame pour lire la manette
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            self.get_logger().error("Aucune manette détectée.")
            return

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.get_logger().info(f"Manette détectée: {self.joystick.get_name()}")

        # Initialisation du publisher ROS 2
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

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

        # Log pour débogage
        self.get_logger().info(f"Vitesse: {vitesse}, Angle: {angle}, Rotation: {droite_x}")

        # Appel de la méthode direction_mecanum
        direction_mecanum(vitesse * 100, angle, droite_x * 100)  # Multiplier par 100 pour ajuster la vitesse

        # Créer un message Twist pour la commande
        cmd_vel = Twist()
        cmd_vel.linear.x = vitesse  # Utilisation de la vitesse linéaire sur l'axe X
        cmd_vel.angular.z = math.radians(angle)  # Convertir l'angle en radians et l'appliquer à la rotation

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
