#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PointStamped

def point_callback(msg):
    rospy.loginfo("Point clicked: x=%f, y=%f, z=%f", msg.point.x, msg.point.y, msg.point.z)

def listener():
    rospy.init_node('point_listener', anonymous=True)
    rospy.Subscriber("/clicked_point", PointStamped, point_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
