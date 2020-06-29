#! /usr/bin/env python

import rospy
import actionlib
from std_msgs.msg import Float64
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
import math, time
import numpy as np
def move_joint(angles):
    goal = FollowJointTrajectoryGoal()
    goal.trajectory.joint_names = ['joint_1', 'joint_2','joint_3' ,'joint_4', 'joint_5', 'joint_6']
    point = JointTrajectoryPoint()
    point.positions = angles
    point.time_from_start = rospy.Duration(3)
    goal.trajectory.points.append(point)
    client.send_goal_and_wait(goal)

if __name__ == '__main__':
    rospy.init_node('joint_position')
    client = actionlib.SimpleActionClient('abb_irb2600_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
    client.wait_for_server()
    rate = rospy.Rate(10)
    i = 0
    while not rospy.is_shutdown():
        move_joint([np.sin(2*np.pi*20*i), 0.5*np.sin(np.pi/12*100*i), 0, np.pi*np.sin(2*np.pi*20*i), np.sin(2*np.pi*20*i), 0])
        i += 0.01
        rate.sleep()
