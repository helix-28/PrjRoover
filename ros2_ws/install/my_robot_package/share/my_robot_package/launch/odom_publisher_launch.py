from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_robot_package',
            executable='odom_publisher_node',
            output='screen',
            name='odom_publisher_node'
        ),
    ])
