import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vikmo/roover_ws/PrjRoover/ros2_ws/install/my_robot_package'
