import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Déclarer un argument de lancement pour le mode de fonctionnement
        DeclareLaunchArgument('robot_mode', default_value='auto', description='Mode de fonctionnement du robot'),

        # Lancer joy_to_cmd_vel pour convertir les entrées du joystick en commandes cmd_vel
        Node(
            package='my_robot_package',  # Remplace avec ton nom de package
            executable='joy_to_cmd_vel',  # Le script qui traite les entrées du joystick
            name='joy_to_cmd_vel_node',
            output='screen',
            parameters=[{'robot_mode': LaunchConfiguration('robot_mode')}]
        ),

        # Lancer cmd_vel_to_motors pour envoyer les commandes au moteur
        Node(
            package='my_robot_package',  # Remplace avec ton nom de package
            executable='cmd_vel_to_motors',  # Le script qui contrôle les moteurs
            name='cmd_vel_to_motors_node',
            output='screen',
        ),
    ])
