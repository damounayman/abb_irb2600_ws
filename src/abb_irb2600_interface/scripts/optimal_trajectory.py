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

    arm_group.go(joint_goal, wait=True)
    arm_group.stop() # To guarantee no residual movement
def fourier(t,w_f,n_H,q_0,a,b):
    p1 = np.sum(a)*math.sin(w_f*t)
    p2 = np.sum(b)*math.cos(w_f*t)
    return q_0+(1/w_f)*(p1+p2)

if __name__ == '__main__':

    # Print current robot state
    print "============ Printing robot state ============"
    print robot.get_current_state()
    print ""
    a1 = [0.4224, 0.7427, -0.7296, 0.1683, -0.7145, -0.3165]
    b1 = [0.9566, 0.2455, 0.1097, 0.1063, 0.0498, 0.5324]
    a2 = [-0.0979, 0.2547, -1.4984, -0.1893, 0.7601, 0.3814 ]
    b2 = [0.6919, -0.2631, 0.2166, -0.2469, 1.2738, 0.5826]
    a3 = [1.0303, 0.4103, -0.0806,1.2594, -0.134, 0.0332]
    b3 = [-2.5898, -0.6318, 0.9551, 4.2279, -0.6559, 1.5114]
    a4 = [0.2204, -0.4595, -0.7599, 1.5698, -1.7115, 0.4964]
    b4 = [-0.5062, 1.5459, 1.5592, 0.3073, 1.0485, 1.0274]
    a5 = [-0.3146, 5.6065, 0.5545, 0.439, -0.2219, 0.0792]
    b5 = [0.6319, -3.7949, -0.2665, -0.358, -0.3345, 1.4024]
    a6 = [0.4224, 0.7427, -0.7296, 0.1683, -0.7145, -0.3165]
    b6 = [0.9566, 0.2455, 0.1097, 0.1063, 0.0498, 0.5324]
    q0 = [0.4449, -1.6626, -1.1696, 0.3969,-0.1445, -0.1445]
    msg1 = Float64()
    msg2 = Float64()
    msg3 = Float64()
    msg4 = Float64()
    msg5 = Float64()
    msg6 = Float64()
    while not rospy.is_shutdown():
        #n = 200
        #dt = 0.01
          wf=2*pi*0.001
        #for i in range (n):
          msg1.data = fourier(time.time(),wf,6,q0[0],a1,b1)
          msg2.data = fourier(time.time(),wf,6,q0[1],a2,b2)
          msg3.data = fourier(time.time(),wf,6,q0[2],a3,b3)
          msg4.data = fourier(time.time(),wf,6,q0[3],a4,b4)
          msg5.data = fourier(time.time(),wf,6,q0[4],a5,b5)
          msg6.data = fourier(time.time(),wf,6,q0[5],a6,b6)
          move_joint_arm(msg1.data,msg2.data,msg3.data,0,0,0)
          time.sleep(0.1)


    rospy.loginfo("All movements finished. Shutting down")
    moveit_commander.roscpp_shutdown()
