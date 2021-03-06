#!/usr/bin/env python
import roslib; roslib.load_manifest('assign5')
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math
import random

global ip
global ip1
global ip2
global ip3
pub=rospy.Publisher('/robot/cmd_vel',Twist,queue_size=5)
ip = []
ip1 = []
ip2 = []
ip3 = []
# definition of normal curve
def gauss (x, mu, sigma):
    exp= 0 - (((float(x)-float(mu))** 2) / (2 * float(sigma) * float(sigma)))
    return (1/(float(sigma) * math.sqrt(2*math.pi))) * (math.e ** exp)

# this experimentally approximates door sensor performance
def door(mu, x):
    sigma= .75
    peak= gauss(0, 0, sigma)   
    return 0.8 * gauss(x, mu, sigma)/peak

# doors are centered at 11m, 18.5m, and 41m
def p_door(x):
    return 0.1 + door(11, x) + door(18.5, x) + door(41, x)

def p_wall(x):
    return 1.0 - p_door(x)

def talker(data):
	#print data.data	
	sum=0
	msg = Twist()
	msg.linear.x=4
	pub.publish(msg)
	for a in range(0,599):     #motion model / intial sampling
		for b in range(a,a+4):
			ip[b] =ip[b] + (40*gauss(b-a,msg.linear.x,4/3))
			if ip[b]>599:
				ip[b]=random.randint(0,600)
	for i in range(0,599):		#measurement model
		ip1[i]=ip1[i]*p_door(ip[i]/10)
		sum=sum+ip1[i]
	for j in range(0,599):
		ip1[j]=ip1[j]/sum
	for a in range(0,599):	#resampling
		temp = random.uniform(0,1.0/600.0)
		c=ip1[0]
		t=0
		for f in range (1,599):
			u=temp+(f-1)*(1.0/600.0)
			while u>c:
				t=t+1
				c=c+ip1[t]
			ip2[f]=ip[f]	#o/p of resampling					
		
	for k in range(0,599):
		ip3[k]='%.6f *'%ip2[k]
	
	print ip2	
	print ip3
def listener():
	rospy.init_node('ListenerTalker',anonymous=True)
	rospy.Subscriber('/robot/wall_door_sensor', String,talker)
	rospy.spin()

if __name__=='__main__':
	for i in range(0,599):
		ip.append(random.randint(0,599))
		ip1.append(1.0/600.0)
		ip2.append(0)
		ip3.append('_')
	for j in range(600,605):
		ip.append(0)
	listener()
