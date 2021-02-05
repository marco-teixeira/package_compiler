cmake_minimum_required(VERSION 2.8.3)
project(package_compiler)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)


generate_messages(
  DEPENDENCIES
    std_msgs
)


catkin_package(
  CATKIN_DEPENDS
    std_msgs
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


