#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import String
from random import randrange,randint
a = []
size = 17
AvailPose = []

def Lab_init():
    global a
    a = []
    a.append([])
    for y in range(size):
        a[0].append(1)
    for i in range(1,size-1):
        a.append([])
        for b in range(size):
            if b == 0 or b == 16:
                a[i].append(1)
            else:
                a[i].append(randint(0,1))
    a.append([])
    for y in range(size):
                a[16].append(1)

def robot_init():
    global RI,RJ,pose
    while True:
        RI = randrange(1,16)
        RJ = randrange(1,16) #upfordebate could go with checking all empty spots then random
        if a[RI][RJ] == 0:
            pose = [RI,RJ]
            break


def updatePose():
    global AvailPose,pose,RI,RJ
    if a[RI][RJ-1] == 0:
        AvailPose.append([RI,RJ-1])
    if a[RI][RJ+1] == 0:
        AvailPose.append([RI,RJ+1])
    if a[RI+1][RJ] == 0:
        AvailPose.append([RI+1,RJ])
    if a[RI-1][RJ] == 0:
        AvailPose.append([RI-1,RJ])
    if len(AvailPose):
        pose = AvailPose[randrange(len(AvailPose))]
        RI = pose[0]
        RJ = pose[1]
    AvailPose = []

def callback(msg):
    pub.publish("alpha " + position)


if __name__ == '__main__': 
    rospy.init_node("alpha")
    pub = rospy.Publisher("robo_info_alpha",String,queue_size=100)
    sub = rospy.Subscriber("robo_info",String,callback)

    Lab_init()
    robot_init()
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        updatePose()
        position = "x=%d,y=%d" % (pose[0],pose[1])
        rospy.loginfo(position)
        rate.sleep()