# This is an auto generated Dockerfile for ros:ros1-bridge
# generated from docker_images_ros2/ros1_bridge/create_ros_ros1_bridge_image.Dockerfile.em
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

# Setup peanut stack 
RUN mkdir -p ~/peanut2_ws/src
RUN cd ~/peanut2_ws/src && \
    git clone https://github.com/peanut-robotics/peanut_ros2.git && \
    cd ~/peanut2_ws/src/peanut_ros2 && git checkout features/navigation2/setup
RUN cd ~/peanut2_ws && \
    . /opt/ros/foxy/setup.sh && \
    colcon build --symlink-install

# Setup ros bridge source files 
RUN mkdir -p ~/bridge_ws/src 
RUN cd ~/bridge_ws/src && git clone https://github.com/ros2/ros1_bridge.git 
RUN cd ~/bridge_ws/src/ros1_bridge && git checkout foxy
RUN cd ~/bridge_ws && \
    . /opt/ros/noetic/setup.sh && \ 
    . /opt/ros/foxy/setup.sh && \
    colcon build --symlink-install

# Copy scripts
COPY ./source_peanut2.sh /
COPY ./source_bridge.sh / 
