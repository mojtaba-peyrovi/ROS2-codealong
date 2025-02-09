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


