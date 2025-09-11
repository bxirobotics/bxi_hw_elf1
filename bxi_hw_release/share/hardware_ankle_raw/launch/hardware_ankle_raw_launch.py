import os
from ament_index_python.packages import get_package_share_path
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription(
        [
            Node(
                package="hardware_ankle_raw",
                executable="hardware_ankle_raw",
                name="hardware_ankle_raw",
                output="screen",
                parameters=[
                    # {"simulation/model_file": xml_file},
                ],
                emulate_tty=True,
                arguments=[("__log_level:=debug")],
            ),
        ]
    )
