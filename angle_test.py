import pypot.dynamixel
import time
from math import *

fire_ids=[2,4,6]
armangle=90

d=.06
head = float(raw_input())
arm = degrees(atan((sin(head*pi/180)-d)/ cos(head*pi/180)))


ports = pypot.dynamixel.get_available_ports()
if not ports :
	raise IOError("port bhakchodi pel rahe hain")

print "Is port se judna hai",ports[0]

dxl = pypot.dynamixel.DxlIO(ports[0])
ids = dxl.scan(range(20))
print ids
dxl.set_goal_position({19: head+47})
dxl.set_goal_position({2:0})
time.sleep(0.01)
dxl.set_goal_position({4:180+arm})

print arm,head
#print dxl.get_present_position([4])
#dxl.enable_torque(ids)
