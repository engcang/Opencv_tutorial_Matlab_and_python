# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:10:26 2018

@author: mason
"""

#!/usr/bin/env python
"""
Created on Fri Nov  9 10:25:22 2018

@author: mason
"""
'''libraries'''
import time
import numpy as np
import rospy
import roslib
import cv2
import sys
import signal

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import CompressedImage
from tf.transformations import euler_from_quaternion, quaternion_from_euler

global LSD
LSD = cv2.createLineSegmentDetector(0)

def signal_handler(signal, frame): # ctrl + c -> exit program
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

''' class '''
class robot():
    def __init__(self):
        rospy.init_node('robot_controller', anonymous=True)
        self.img_subscriber = rospy.Subscriber('/raspicam_node/image/compressed',CompressedImage,self.callback_img)

    def callback_img(self,data):
        np_arr = np.fromstring(data.data, np.uint8)
        self.image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR) # OpenCV >= 3.0:
        
    def keeping(self,hsv,img):
        global LSD
        crop_L=hsv[350:410,40:220]
        crop_R=hsv[350:410,402:582]
        L_mask = cv2.inRange(crop_L,(36,0,165),(255,255,255))
        R_mask = cv2.inRange(crop_R,(21,50,100),(36,255,255))
      
        index_L_mask = L_mask>0
        index_R_mask = R_mask>0
    
        yello=np.zeros_like(crop_L,np.uint8)
        white=np.zeros_like(crop_R,np.uint8)
        yello[index_L_mask]= crop_L[index_L_mask]
        white[index_R_mask]=crop_R[index_R_mask]
        cv2.imshow('masked1',yello)
        cv2.waitKey()
        cv2.imshow('masked2',white)
        cv2.waitKey()
        yello_line = LSD.detect(L_mask)
        white_line = LSD.detect(R_mask)
        LSD.drawSegments(img[350:410,40:220],yello_line[0])
        LSD.drawSegments(img[350:410,402:582],white_line[0])
        cv2.imshow('Lines',img[350:410,:])
        cv2.waitKey()

    def imageupdate(self):
        image=self.image_np
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        return image,hsv
        
turtle=robot()
time.sleep(1.2)
if __name__=='__main__':
        try:
            img,hsv=turtle.imageupdate()
            cv2.imshow('raw',img)
            cv2.waitKey()
            turtle.keeping(hsv,img) 
        except (KeyboardInterrupt, SystemExit):
            sys.exit(0)
        except :
            print('got error')