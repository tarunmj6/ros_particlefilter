# ros_particlefilter
A python program to make ros simulated robot localize using particle filter algorithm

The starter code is available from https://github.com/DeepBlue14/uml_hmm. Under scripts there is a python file "mcl.py" which localizes the robot in the map given from left to right. The python code subcribes to "/robot/wall_door_sensor" topics to get the sensor reading of the robot and publishes the speed and rotation to the topic "/robot/cmd_vel". The ouput is an array which provides the position of the particles where the robot is localized

To run this simulation on one node(terminal) run "roslaunch ros_gridlocalization hmm.launch" which opens the racetrack and on another node run "rosrun ros_gridlocaliztion histogram.py" which makes the robot move and localizes its position.
