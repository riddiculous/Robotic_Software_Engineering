#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(1) # 10hz
	num = 0
	while not rospy.is_shutdown():
		num = num + 1
   		hello_str = "1711524 %s" % str(num)#rospy.get_time()
   		rospy.loginfo(hello_str)
   		pub.publish(hello_str)
   		rate.sleep()
		

if __name__ == '__main__':
	try:
   		talker()
	except rospy.ROSInterruptException:
   		pass

