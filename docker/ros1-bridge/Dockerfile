# Peanut Dockerfile
ARG PEANUT_WS=~/peanut2_ws
ARG NAV2_WS=~/navigation2_ws
ARG BRIDGE_WS=~/bridge_ws

FROM ros:foxy

# setup keys
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# setup sources.list
RUN echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros1-latest.list

ENV ROS1_DISTRO noetic
ENV ROS2_DISTRO foxy

# install ros packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-ros-comm=1.15.8-1* \
    ros-noetic-roscpp-tutorials=0.10.2-1* \
    ros-noetic-rospy-tutorials=0.10.2-1* \
    && rm -rf /var/lib/apt/lists/*

# install ros2 packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-foxy-demo-nodes-cpp=0.9.3-1* \
    ros-foxy-demo-nodes-py=0.9.3-1* \
    && rm -rf /var/lib/apt/lists/*

# Add keys 
RUN sudo apt update 
RUN sudo apt install -y curl gnupg2 lsb-release && \
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
RUN sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
RUN sudo apt update 

# Setup peanut stack 
ARG PEANUT_WS
RUN mkdir -p ~/peanut2_ws/src
RUN cd ~/peanut2_ws/src && \
    git clone https://github.com/peanut-robotics/peanut_ros2.git && \
    cd ~/peanut2_ws/src/peanut_ros2 && git checkout features/navigation2/setup
RUN cd ~/peanut2_ws && \
    . /opt/ros/foxy/setup.sh && \
    colcon build --symlink-install

# Setup navigation stack 
ARG NAV2_WS
RUN mkdir -p ~/navigation2_ws/src
RUN cd ~/navigation2_ws/src && git clone https://github.com/ros-planning/navigation2.git --branch foxy-devel
RUN cd ~/navigation2_ws && \
    . /opt/ros/foxy/setup.sh && \
    rosdep install -y -r -q --from-paths src --ignore-src --rosdistro foxy && \
    colcon build --symlink-install

# Setup ros bridge source files 
ARG BRIDGE_WS
RUN mkdir -p ~/bridge_ws/src 
RUN cd ~/bridge_ws/src && git clone https://github.com/ros2/ros1_bridge.git 
RUN cd ~/bridge_ws/src/ros1_bridge && git checkout foxy
RUN cd ~/bridge_ws && \
    . /opt/ros/noetic/setup.sh && \ 
    . /opt/ros/foxy/setup.sh && \
    . ~/peanut2_ws/install/setup.sh && \
    . ~/navigation2_ws/install/setup.sh && \
    colcon build --symlink-install

# Copy scripts
COPY ./source_peanut2.sh /
COPY ./source_bridge.sh / 
