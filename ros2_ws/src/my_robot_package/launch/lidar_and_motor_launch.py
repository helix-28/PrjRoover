import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get the path to the rplidar_c1_launch.py
    rplidar_launch_file = os.path.join(
        get_package_share_directory('rplidar_ros'),
        'launch',
        'rplidar_c1_launch.py'
    )

    return LaunchDescription([
        # RPLIDAR launch
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(rplidar_launch_file),
            launch_arguments={
                'serial_port': '/dev/ttyUSB0',
                'serial_baudrate': '115200'
            }.items()
        ),

        # Motor control node
        Node(
            package='my_robot_package',
            executable='cmd_vel_to_motors',
            name='cmd_to_motor',
            output='screen',
        ),
    ])

