from setuptools import setup

package_name = 'odom_publisher'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    py_modules=['odom_publisher.odom_publisher_node'],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Your Name',
    author_email='your_email@example.com',
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='A simple odom publisher to publish odom transform from cmd_vel',
    license='License type (e.g., MIT)',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'odom_publisher_node = odom_publisher.odom_publisher_node:main',
        ],
    },
)

