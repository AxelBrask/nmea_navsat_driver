#!/usr/bin/python

import rospy 
import numpy as np
from sensor_msgs.msg import NavSatFix


class FixGPS(object):

    def cb(self, gps_msg):
        gps_msg.header.frame_id = 'sam/gps_link'
        self.pub.publish(gps_msg)

    def __init__(self):
        self.sub = rospy.Subscriber('/sam/core/gps', NavSatFix, self.cb) 
        self.pub = rospy.Publisher('/sam/core/gps_amm', NavSatFix, queue_size=10)
        rospy.spin()

if __name__ == "__main__":
    rospy.init_node('fix_gps_link')
    try:
        FixGPS()
    except rospy.ROSInterruptException:
        pass 
