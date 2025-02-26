# ROS2-codealong
My personal effort to understand how coding for robots works.


Reference: https://youtu.be/0aPbWsyENA8?si=LgSKr2kZ6KMCcn37

__Part 1:__  Installed the app on Ubuntu WSL on Windows following this doc:
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html



__Part 2:__  
We can create sample nodes like 'talker' and 'listener' running the following:

```
ros2 run demo_nodes_cpp talker

& 

ros2 run demo_nodes_cpp listener
```

To see all running nodes we can run:

```
rqt_graph
```

while both nodes are running and the graph is on, we can see that the talker and listener are talking to each other through "chatter" which is a topic.


We can use the "turtlesim" simulator for testing. 

```
ros2 run turtlesim turtlesim_node
```

### Part 3: How to create a ROS2 workspace?

1- First we need to install the ROS build tool.

```
sudo apt install python3-colcon-common-extensions
```
2- Create a workspace directory inside the project dir and inside the workspace, make another directory called "src". It cannot be another name. While inside the workspace dir, run:

```
colcon build
```
3- There will be a few folders created under the workspace folder and one of them is called "install" and there is a setup.bash file which will source it and it can install all requirements.

Now we are ready!


### Part 4: Create a package

1- first cd to the workspace folder and the "src" subfloder:

```
cd ros2_ws/src
```

2- run the following:

```
ros2 pkg create my_robot_controller --build-type ament_python --dependencies rclpy
```

rclpy is a ros2 python library. 

- The hierarchy of a project is workspace/package/nodes

- Sometimes we will have dependencies between the packages. 


3- finally we need to get back to the workspace folder and run:
```
colcon build
```

Now we have all we need to start writing some code!


### Part 5: Create the first node

The first node is created inside ros2_ws/src/my_robot_controller/my_robot_controller/my_First_node.py.

The code can run via terminal when we just say:  python3 my_first_node.py.  But now we want to run it as a ROS2 script and for this we need to convert the node into a package. It can happen inside setup.py and the name of the package should be added under "entry_points" like the following:
```
name of the node = <package_name>:<py file name>:<function name>

test_node = test_node= my_first_controller.my_first_controller:main
```

Finally, we need to run the following in the terminal to get the node built:

````
colcon build  & source ~/.bashrc
```

The way we did, we need to do colcon build after any change. But this is the way to bypass it after each change. 

```
colcon build --symlink-install
```

after we run this, it builds once and afterwards, the next times it would do the build by itself and we dont need to do it manually. 

After the build we need to source the workspace by running:
'''
source ~/ros2_ws/install/setup.bash
'''



