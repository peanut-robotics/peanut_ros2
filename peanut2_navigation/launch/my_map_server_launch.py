from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="nav2_map_server",
            executable="map_server",
            name="my_map_server",
            output="screen",
            emulate_tty=True,
            parameters=[
                {"yaml_filename": "/home/peanut/peanut2_ws/src/peanut_ros2/peanut2_navigation/maps/office.yaml"}
            ]
        )
    ])
