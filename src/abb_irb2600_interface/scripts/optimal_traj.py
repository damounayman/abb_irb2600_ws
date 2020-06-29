#!/usr/bin/env python

import roslib
import rospy, math, time
from math import pi
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def jointTrajectoryCommand():
    # Initialize the node
    rospy.init_node('joint_control')

    print rospy.get_rostime().to_sec()
    while rospy.get_rostime().to_sec() == 0.0:
        time.sleep(0.1)
        print rospy.get_rostime().to_sec()

    pub = rospy.Publisher('/abb_irb6640_controller/command', JointTrajectory, queue_size=10)
    jt = JointTrajectory()

    jt.header.stamp = rospy.Time.now()
    jt.header.frame_id = "abb_irb6640"

    jt.joint_names.append("joint_1")
    jt.joint_names.append("joint_2")
    jt.joint_names.append("joint_3")
    jt.joint_names.append("joint_4")
    jt.joint_names.append("joint_5")
    jt.joint_names.append("joint_6")



    n = 15
    dt = 0.01
    rps = 0.05
    for i in range (n):
        p = JointTrajectoryPoint()
        #theta = rps*2.0*math.pi*i*dt
        #x1 = -0.5*math.sin(2*theta)
        #x2 =  0.5*math.sin(1*theta)

        p.positions.append(pi/2)
        p.positions.append(0)
        p.positions.append(0)
        p.positions.append(0)
        p.positions.append(0)
        p.positions.append(0)
        jt.points.append(p)

        # set duration
        jt.points[i].time_from_start = rospy.Duration.from_sec(dt)
        #rospy.loginfo("test: angles[%d][%f, %f]",n,x1,x2)

    pub.publish(jt)
    rospy.spin()

if __name__ == '__main__':
    try:
        jointTrajectoryCommand()
    except rospy.ROSInterruptException: pass
