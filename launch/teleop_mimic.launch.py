from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim1',
            namespace='turtlesim1'
        ),

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim2',
            namespace='turtlesim2'
        ),

        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            prefix='xterm -e',
            remappings=[
                ('/turtle1/cmd_vel',
                 '/turtlesim1/turtle1/cmd_vel')
            ]
        ),

        TimerAction(
            period=10.0,
            actions=[
                Node(
                    package='turtlesim',
                    executable='mimic',
                    name='mimic',
                    remappings=[
                        ('/input/pose',
                         '/turtlesim1/turtle1/pose'),
                        ('/output/cmd_vel',
                         '/turtlesim2/turtle1/cmd_vel')
                    ]
                )
            ]
        )

    ])