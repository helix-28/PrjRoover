import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch RPLIDAR C1
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                '/home/vikmo/roover_ws/PrjRoover/ros2_lidar_ws/src/rplidar_ros/launch/rplidar_c1_launch.py'
            ),
            launch_arguments={'serial_port': '/dev/ttyUSB0', 'serial_baudrate': '115200'}.items()
        ),
        
        # Launch cmd_to_motor (your motor control node)
        Node(
            package='my_robot_package',  # Replace with your package name
            executable='cmd_vel_to_motors',  # Replace with your script or executable name
            name='cmd_to_motor',
            output='screen',
        ),
    ])
