import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import RPi.GPIO as GPIO


class CmdVelToMotors(Node):
    def __init__(self):
        super().__init__('cmd_vel_to_motors')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10
        )
        self.setup_gpio()

    def setup_gpio(self):
        self.moteurF_AVNT_DRT = 23
        self.moteurR_AVNT_DRT = 24
        self.moteurF_AVNT_GCH = 25
        self.moteurR_AVNT_GCH = 5
        self.moteurF_ARR_DRT = 4
        self.moteurR_ARR_DRT = 17
        self.moteurF_ARR_GCH = 27
        self.moteurR_ARR_GCH = 22

        self.NSLEEP1 = 18
        self.NSLEEP2 = 13
        self.NSLEEP3 = 12
        self.NSLEEP4 = 19

        GPIO.setmode(GPIO.BCM)
        for pin in [self.NSLEEP1, self.NSLEEP2, self.NSLEEP3, self.NSLEEP4,
                    self.moteurF_AVNT_DRT, self.moteurR_AVNT_DRT,
                    self.moteurF_AVNT_GCH, self.moteurR_AVNT_GCH,
                    self.moteurF_ARR_DRT, self.moteurR_ARR_DRT,
                    self.moteurF_ARR_GCH, self.moteurR_ARR_GCH]:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        self.p1 = GPIO.PWM(self.NSLEEP1, 1000)
        self.p2 = GPIO.PWM(self.NSLEEP2, 1000)
        self.p3 = GPIO.PWM(self.NSLEEP3, 1000)
        self.p4 = GPIO.PWM(self.NSLEEP4, 1000)

        self.p1.start(25)
        self.p2.start(25)
        self.p3.start(25)
        self.p4.start(25)

    def listener_callback(self, msg):
        vitesse = msg.linear.x * 100
        angle = math.degrees(msg.angular.z)
        rot = msg.linear.z
        self.get_logger().info(f"cmd_vel reçu : vitesse={vitesse:.2f}, angle={angle:.2f}, rot = {rot:.2f}")
        self.direction_mecanum(vitesse, angle, rot)

    def direction_mecanum(self, vitesse, angle, rotation):
        vx = vitesse * math.cos(math.radians(angle))
        vy = vitesse * math.sin(math.radians(angle))

        v_AVNT_DRT = vx + vy + rotation
        v_AVNT_GCH = vx - vy - rotation
        v_ARR_DRT = vx - vy + rotation
        v_ARR_GCH = vx + vy - rotation

        max_val = max(abs(v_AVNT_DRT), abs(v_AVNT_GCH), abs(v_ARR_GCH), abs(v_ARR_DRT))
        if max_val > 100:
            v_AVNT_DRT = v_AVNT_DRT / max_val * 100
            v_AVNT_GCH = v_AVNT_GCH / max_val * 100
            v_ARR_DRT = v_ARR_DRT / max_val * 100
            v_ARR_GCH = v_ARR_GCH / max_val * 100

        self.set_motor(self.moteurF_AVNT_DRT, self.moteurR_AVNT_DRT, v_AVNT_DRT, self.p1)
        self.set_motor(self.moteurF_AVNT_GCH, self.moteurR_AVNT_GCH, v_AVNT_GCH, self.p2)
        self.set_motor(self.moteurF_ARR_DRT, self.moteurR_ARR_DRT, v_ARR_DRT, self.p4)
        self.set_motor(self.moteurF_ARR_GCH, self.moteurR_ARR_GCH, v_ARR_GCH, self.p3)

    def set_motor(self, pin_fwd, pin_rev, speed, pwm):
        if speed > 0:
            GPIO.output(pin_fwd, GPIO.HIGH)
            GPIO.output(pin_rev, GPIO.LOW)
        elif speed < 0:
            GPIO.output(pin_fwd, GPIO.LOW)
            GPIO.output(pin_rev, GPIO.HIGH)
        else:
            GPIO.output(pin_fwd, GPIO.LOW)
            GPIO.output(pin_rev, GPIO.LOW)
        pwm.ChangeDutyCycle(min(abs(speed), 100))


def main(args=None):
    rclpy.init(args=args)
    node = CmdVelToMotors()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
        GPIO.cleanup()


if __name__ == '__main__':
    main()
