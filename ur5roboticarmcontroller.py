#!/usr/bin/env python
import sys,rospy,moveit_commander,tf,random 
from geometry_msgs.msg import Pose,Point,Quaternion  #library for geometry calculation
from math import pi   #import pi for for calculation in the math 

orient = [Quaternion(tf.transformations.quaternion_from_euler(pi,-pi/2,-pi/2)),
          Quaternion(tf.transformations.quaternion_from_euler(pi,-pi/2,-pi/2))]

pose = [Pose(Point(0.5,-0.5,1.3),orient[0]),
        Pose(Point(-0.5,-0.5),orient[1])]
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur5roboticarmwiththewallsw',anonymous=True)
group = [moveit_commander.MoveGroupCommander("Baserotation_Link"),
         moveit_commander.MoveGroupCommander("Uppershoulder_Link"),
         moveit_commander.MoveGroupCommander("Elbow_Link"),
         moveit_commander.MoveGroupCommander("Wristrotation_Link"),
         moveit_commander.MoveGroupCommander("Wrist_Link"),
         moveit_commander.MoveGroupCommander("Handrotation_Link"),
         moveit_commander.MoveGroupCommander("Finger1U_Link"),
         moveit_commander.MoveGroupCommander("Finger1E_Link"),
         moveit_commander.MoveGroupCommander("Finger2_Link"),
         moveit_commander.MoveGroupCommander("Finger2U_Link"),
         moveit_commander.MoveGroupCommander("Finger2E_Link"),
         moveit_commander.MoveGroupCommander("Finger3_Link"),
         moveit_commander.MoveGroupCommander("Finger3U_Link"),
         moveit_commander.MoveGroupCommander("Finger3E_Link")]
 
while not rospy.is_shutdown():

    pose[0].position.x =  0.5 + random.uniform(-0.1,0.1) 
    pose[1].position.y = -0.5 + random.uniform(-0.1,0.1) 
for side in [0,1]:
    pose[side].position.z = 1.5 + random.uniform(-0.1,0.1)  
    group[side].set_pose_target(pose[side])
    group[side].go(True) 
     

moveit_commander.roscpp_shutdown()

 
      
       
 

