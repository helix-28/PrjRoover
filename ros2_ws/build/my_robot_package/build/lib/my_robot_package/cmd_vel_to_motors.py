import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TransformStamped
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from rclpy.qos import QoSProfile
import math
import RPi.GPIO as GPIO
import time


class CmdVelToMotors(Node):
    def __init__(self):
        super().__init__('cmd_vel_to_motors')

        qos = QoSProfile(depth=10)

        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            qos
        )

        self.odom_publisher = self.create_publisher(Odometry, '/odom', qos)
        self.tf_broadcaster = TransformBroadcaster(self)

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.last_time = self.get_clock().now()

        self.linear_velocity = 0.0
        self.angular_velocity = 0.0

        self.setup_gpio()
        self.timer = self.create_timer(0.05, self.publish_odom)  # 20 Hz

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
        self.linear_velocity = msg.linear.x
        self.angular_velocity = msg.angular.z
        self.direction_mecanum(self.linear_velocity * 100, math.degrees(self.angular_velocity), 0)

    def publish_odom(self):
        now = self.get_clock().now()
        dt = (now - self.last_time).nanoseconds / 1e9
        self.last_time = now

        dx = self.linear_velocity * math.cos(self.theta) * dt
        dy = self.linear_velocity * math.sin(self.theta) * dt
        dtheta = self.angular_velocity * dt

        self.x += dx
        self.y += dy
        self.theta += dtheta

        # TF transform
        t = TransformStamped()
        t.header.stamp = now.to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'
        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.translation.z = 0.0
        q = self.quaternion_from_yaw(self.theta)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        self.tf_broadcaster.sendTransform(t)

        # Odometry message
        odom = Odometry()
        odom.header.stamp = now.to_msg()
        odom.header.frame_id = 'odom'
        odom.child_frame_id = 'base_link'
        odom.pose.pose.position.x = self.x
        odom.pose.pose.position.y = self.y
        odom.pose.pose.position.z = 0.0
        odom.pose.pose.orientation.x = q[0]
        odom.pose.pose.orientation.y = q[1]
        odom.pose.pose.orientation.z = q[2]
        odom.pose.pose.orientation.w = q[3]
        odom.twist.twist.linear.x = self.linear_velocity
        odom.twist.twist.angular.z = self.angular_velocity

        self.odom_publisher.publish(odom)

    def quaternion_from_yaw(self, yaw):
        return (0.0, 0.0, math.sin(yaw / 2.0), math.cos(yaw / 2.0))

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
