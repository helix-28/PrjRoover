#!/usr/bin/env python3

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'channel_type',
            default_value='serial',
            description='Specifying channel type of lidar'),

        DeclareLaunchArgument(
            'serial_port',
            default_value='/dev/ttyUSB0',
            description='Specifying usb port to connected lidar'),

        DeclareLaunchArgument(
            'serial_baudrate',
            default_value='115200',  # C1 default
            description='Specifying usb port baudrate to connected lidar'),

        DeclareLaunchArgument(
            'frame_id',
            default_value='laser',
            description='Specifying frame_id of lidar'),

        DeclareLaunchArgument(
            'inverted',
            default_value='false',
            description='Specifying whether or not to invert scan data'),

        DeclareLaunchArgument(
            'angle_compensate',
            default_value='true',
            description='Specifying whether or not to enable angle_compensate of scan data'),

        DeclareLaunchArgument(
            'scan_mode',
            default_value='Standard',
            description='Specifying scan mode of lidar'),

        Node(
            package='rplidar_ros',
            executable='rplidar_node',
            name='rplidar_node',
            output='screen',
            parameters=[{
                'channel_type': LaunchConfiguration('channel_type'),
                'serial_port': LaunchConfiguration('serial_port'),
                'serial_baudrate': LaunchConfiguration('serial_baudrate'),
                'frame_id': LaunchConfiguration('frame_id'),
                'inverted': LaunchConfiguration('inverted'),
                'angle_compensate': LaunchConfiguration('angle_compensate'),
                'scan_mode': LaunchConfiguration('scan_mode'),
            }]
        ),
    ])

