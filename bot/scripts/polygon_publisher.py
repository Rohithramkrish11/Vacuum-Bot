#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PointStamped
import yaml
import os

def publish_points(points):
    for point in points:
        p = PointStamped()
        p.header.frame_id = "map"
        p.header.stamp = rospy.Time.now()
        p.point.x = point[0]
        p.point.y = point[1]
        p.point.z = point[2]  # Include the z coordinate
        point_pub.publish(p)
        rospy.sleep(0.1)  # Small delay to ensure proper publishing

def main():
    rospy.init_node('automatic_polygon_publisher', anonymous=True)
    global point_pub
    point_pub = rospy.Publisher('/clicked_point', PointStamped, queue_size=10)

    # Load room coordinates from YAML file
    room_coordinates_file = rospy.get_param("~room_coordinates_file")
    room_coordinates_file = os.path.expanduser(room_coordinates_file)  # Expand the tilde manually

    with open(room_coordinates_file, 'r') as f:
        rooms = yaml.safe_load(f)

    rate = rospy.Rate(1)  # 1 Hz

    for room_name, points in rooms['rooms'].items():
        rospy.loginfo(f"Publishing points for {room_name}")
        publish_points(points)

    rospy.loginfo("All points published. Waiting for path coverage to complete.")

    # rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

