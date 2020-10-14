# Peanut Dockerfile
FROM peanutrobotics/ros:foxy 

ARG PEANUT_WS=~/peanut2_ws
ARG NAV2_WS=~/navigation2_ws
ARG BRIDGE_WS=~/bridge_ws

# setup keys
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# setup sources.list
RUN echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros1-latest.list

ENV ROS1_DISTRO noetic
ENV ROS2_DISTRO foxy

# Add keys 
RUN sudo apt update  && \
    sudo apt install -y curl gnupg2 lsb-release && \
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
RUN sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

# install ros1 packages
RUN sudo apt update && sudo apt install -y ros-noetic-desktop

# Setup peanut stack 
ARG PEANUT_WS
RUN mkdir -p ~/peanut2_ws/src
RUN cd ~/peanut2_ws/src && \
    git clone https://github.com/peanut-robotics/peanut_ros2.git && \
    cd ~/peanut2_ws/src/peanut_ros2 && git checkout features/navigation2/setup
RUN cd ~/peanut2_ws && \
    . /opt/ros/foxy/setup.sh && \
    colcon build --symlink-install

# Setup ros bridge
ARG BRIDGE_WS
RUN mkdir -p ~/bridge_ws/src 
RUN cd ~/bridge_ws/src && git clone https://github.com/ros2/ros1_bridge.git 
RUN cd ~/bridge_ws/src/ros1_bridge && git checkout foxy
RUN cd ~/bridge_ws && \
    . /opt/ros/noetic/setup.sh && \ 
    . /opt/ros/foxy/setup.sh && \
    . ~/peanut2_ws/install/setup.sh && \
    colcon build --symlink-install

# Setup navigation stack from source  
ARG NAV2_WS
RUN mkdir -p ~/navigation2_ws/src
RUN cd ~/navigation2_ws/src && git clone https://github.com/ros-planning/navigation2.git --branch foxy-devel
RUN cd ~/navigation2_ws && \
    . /opt/ros/foxy/setup.sh && \
    rosdep install -y -r -q --from-paths src --ignore-src --rosdistro foxy && \
    colcon build --symlink-install --cmake-args -DBUILD_TESTING=OFF

# Setup navigation stack
RUN sudo apt install && \
    sudo apt install -y ros-foxy-navigation2 ros-foxy-nav2-bringup '~ros-foxy-turtlebot3-.*'

# Install misc packages 
RUN sudo apt install -y vim 

# Update bashrc 
RUN echo 'source /usr/share/bash-completion/completions/git' >> ~/.bashrc 

# Copy scripts
COPY ./source_peanut2.sh /
COPY ./source_bridge.sh / 
