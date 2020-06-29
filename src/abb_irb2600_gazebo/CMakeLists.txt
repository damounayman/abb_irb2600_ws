cmake_minimum_required(VERSION 2.8.3)
project(abb_irb2600_gazebo)

find_package(catkin REQUIRED COMPONENTS
  abb_irb2600_gazebo
  abb_irb2600_moveit_config
  abb_irb2600_support
  roscpp
  rospy
  std_msgs)

catkin_package()

foreach(dir config launch urdf)
 install(DIRECTORY ${dir}/
         DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach()
