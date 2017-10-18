import pypot.dynamixel
import time
from math import *

fire_ids=[2,4,6]
armangle=90

d=.06
head = int(raw_input())
#arm = degrees(atan((sin(head*pi/180)-d)/ cos(head*pi/180)))


ports = pypot.dynamixel.get_available_ports()
if not ports :
	raise IOError("port bhakchodi pel rahe hain")

print "Is port se judna hai",ports[0]

dxl = pypot.dynamixel.DxlIO(ports[0])
ids = dxl.scan(range(25))
print ids
if head>0:
	arm = head-135
	dxl.set_goal_position({19: head})
	dxl.set_goal_position({2:90})
	time.sleep(0.01)
	dxl.set_goal_position({4:head-135}) 
	dxl.set_goal_position({3:-30})
	time.sleep(0.01)
	dxl.set_goal_position({1:0})
if head<0:
	arm = head+135
	dxl.set_goal_position({19: head})
	dxl.set_goal_position({1:90})
	time.sleep(0.01)
	dxl.set_goal_position({3:head+135}) 
	dxl.set_goal_position({4:30})
	time.sleep(0.01)
	dxl.set_goal_position({2:0})

if head == 0 :
	
	dxl.set_goal_position({19: head})
	time.sleep(0.01)
	dxl.set_goal_position({2:90})
	time.sleep(0.01)
	dxl.set_goal_position({4:head-135})
	time.sleep(0.01)
	dxl.set_goal_position({1:90})
	time.sleep(0.01)
	dxl.set_goal_position({3:head})

print arm,head
#print dxl.get_present_position([4])
#dxl.enable_torque(ids)
