# Vacuum-bot
Autonomous Vacuum-bot with voice command recognition for path planning

## Setup Instructions

1. **Install Ubuntu 20.04 and ROS Noetic:**

   ```bash
   sudo apt update
   sudo apt install ros-noetic-desktop-full
   
2. **Install Required Dependencies:**

   ```bash
   sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
   sudo apt install curl
   sudo apt install ros-noetic-gmapping ros-noetic-map-server ros-noetic-amcl ros-noetic-move-base
   pip install SpeechRecognition pynput keyboard shapely numpy
   sudo apt install libttspico-utils

3. **Set Up the Workspace:** 

   ```bash
   mkdir -p ~/catkin_ws/src
   cd ~/catkin_ws/
   catkin_make
   source devel/setup.bash

 4. **Clone the Packages:**

    ```bash
    cd ~/catkin_ws/src
    git clone https://github.com/Rohithramkrish11/Vacuum-bot.git
    git clone https://gitlab.com/Humpelstilzchen/path_coverage_ros.git
    cd ~/catkin_ws
    catkin_make
    source devel/setup.bash

5. **Running the Vacuum-bot:**

     ```bash
     roslaunch bot gazebo.launch
     rosrun bot voice_command.py

