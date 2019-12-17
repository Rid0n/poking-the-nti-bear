#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import String
i=0
def callback(msg):
	rospy.loginfo(msg.data)

sub = rospy.Subscriber('robo_info_alpha', String, callback)
sub2 = rospy.Subscriber('robo_info_beta', String, callback)

if __name__ == '__main__': 
    rospy.init_node("omega")
    rate = rospy.Rate(10)
    msg = String()
    pub = rospy.Publisher('robo_info', String, queue_size=100)
    while not rospy.is_shutdown():
		pub.publish("yo")
		rate.sleep()