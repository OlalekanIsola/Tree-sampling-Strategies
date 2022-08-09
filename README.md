# Tree-sampling-Strategies
This program was written in ROS for Autonomous Robot to detect plants along a row and turn towards it depending on the specification. I built on this project (https://github.com/etgaro/OSE_Final_Project).

There are two different different Scenarios, one detects and moves toward color red attached to a tree and the other goes to every N plant

These are the steps for color detection:
 1) roscore
 2) roslaunch gazebo_ros empty_world.launch
 3) open python color_detection.py in a terminal
 4) open python tree_run_Trial.py in another terminal
 
 
 These are the steps for every N plant:
 1) roscore
 2) roslaunch gazebo_ros empty_world.launch
 4) open python tree_run_everyN.py
