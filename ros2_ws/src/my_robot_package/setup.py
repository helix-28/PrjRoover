from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'my_robot_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', [
        'launch/lidar_and_motor_launch.py',
        'launch/roover_control.launch.py',
        'launch/roover_slam.launch.py'
    ]),
],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vikmo',
    maintainer_email='vikmo16@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joy_to_cmd_vel = my_robot_package.joy_to_cmd_vel:main',
            'cmd_vel_to_motors = my_robot_package.cmd_vel_to_motors:main',
        ],
    },
)
