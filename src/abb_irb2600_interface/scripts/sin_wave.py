#! /usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import numpy as np
import moveit_msgs.msg
import geometry_msgs.msg
import math, time
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import Float64
# Init stuff
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('moving_irb2600_robot', anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
arm_group = moveit_commander.MoveGroupCommander("manipulator")


# Publish trajectory in RViz
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)

# Forward Kinematics (FK): move the arm by axis values
def move_joint_arm(joint_1,joint_2,joint_3,joint_4,joint_5,joint_6):
    joint_goal = arm_group.get_current_joint_values()
    joint_goal[0] = joint_1
    joint_goal[1] = joint_2
    joint_goal[2] = joint_3
    joint_goal[3] = joint_4
    joint_goal[4] = joint_5
    joint_goal[5] = joint_6

    arm_group.go(joint_goal)
    arm_group.stop()
if __name__ == '__main__':

    # Print current robot state
    print "============ Printing robot state ============"
    print robot.get_current_state()
    print ""
    i = 0
    msg1 = Float64()
    while not rospy.is_shutdown():
          msg1.data = 1*math.cos(pi/4*i)
          i=i+1
          move_joint_arm(msg1.data,0,0,0,0,0)
          time.sleep(0.1)
