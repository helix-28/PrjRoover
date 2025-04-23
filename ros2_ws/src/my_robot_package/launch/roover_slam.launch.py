import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Declare a launch argument for the robot mode (useful if you want to condition nodes)
        DeclareLaunchArgument('robot_mode', default_value='auto', description='Mode de fonctionnement du robot'),

        # Launch the 'joy_to_cmd_vel' node to read joystick input and send to cmd_vel
        Node(
            package='my_robot_package',  # Replace with your actual package name
            executable='joy_to_cmd_vel',
            name='joy_to_cmd_vel_node',
            output='screen',
        ),
        
        # Launch slam_toolbox for online SLAM
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox_node',
            output='screen',
            parameters=[{'slam_mode': True, 'use_sim_time': False}],  # Adjust the parameters based on your needs
            remappings=[('/scan', '/rplidar_node/scan')]  # Map the LIDAR scan topic correctly
        ),

       # Lancer le nœud odom_publisher pour publier /odom et le tf
        Node(
            package='my_robot_package',  # Remplace par le nom correct de ton package
            executable='odom_publisher_node',
            name='odom_publisher_node',
            output='screen',
        ),
        
        # Launch the static transform publisher to provide the transform from laser to base_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'laser'],
            output='screen',
        ),
        
        # Launch RViz with the default SLAM configuration
        Node(
            package='rviz2',  # This is the ROS 2 RViz package
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/opt/ros/jazzy/share/slam_toolbox/rviz/slam_config.rviz'],  # Default SLAM config file
        ),
    ])

