import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Déclare un argument pour le mode robot (utile si tu veux le conditionner dans tes nodes)
        DeclareLaunchArgument('robot_mode', default_value='auto', description='Mode de fonctionnement du robot'),

        # Lance le driver RPLIDAR
        Node(
            package='rplidar_ros',  # Nom du package rplidar
            executable='rplidarNode',
            name='rplidar_node',
            output='screen',
            parameters=[{'serial_port': '/dev/ttyUSB0', 'frame_id': 'laser_frame'}],  # Ajuste le port série si nécessaire
        ),

        # Lance le script moteur avec odométrie
        Node(
            package='my_robot_package',
            executable='cmd_vel_to_motors',
            name='cmd_vel_to_motors_node',
            output='screen',
        ),

        # Lance slam_toolbox (en mode en ligne pour la cartographie)
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox_node',
            output='screen',
            parameters=[{'slam_mode': True, 'use_sim_time': False}],  # Remarques les booleans
            remappings=[('/scan', '/rplidar_node/scan')]  # Le scan LiDAR va être sur ce topic
        ),

        # Lance la transformation des frames
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'laser_frame'],  # Transformation entre laser et base
        ),
    ])

