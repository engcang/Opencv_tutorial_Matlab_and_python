#!/usr/bin/env python
"""
Created on Fri Nov  9 02:42:58 2018
@author: mason
"""

import cv2
import rospy
import roslib
import numpy as np
from sensor_msgs.msg import CompressedImage
import time

global detectors
global incoming
incoming=0

global detector_start
detector_start = cv2.CascadeClassifier('start.xml')
time.sleep(1)

class camera:
    def __init__(self):
        rospy.init_node('sign_detector', anonymous = True)
        self.image_subscriber=rospy.Subscriber('/zed/rgb/image_rect_color/compressed', CompressedImage, self.callback)

    def callback(self, msg):
        global incoming
        np_arr = np.fromstring(msg.data, np.uint8)
        self.image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        incoming = 1

    def img_update(self):
        img=self.image_np
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        return img,hsv
    
    def detector(self,img,hsv):
        global detector_start
        scale=1.2 # resize .*100%, smaller detect more but take longer
        minNeighbors=6 # higer, higer quality, less detection
        bbox_start = detector_start.detectMultiScale(img,scale,minNeighbors)
        if np.shape(bbox_start)[0]!=0:
            if color_pixel_number(hsv,[(170,150,80),(180,255,130)],bbox_start)>300:
                print('start_sign detected')

def color_pixel_number(hsv,color,bbox):
    if np.shape(bbox)[0]>1:
        area=np.zeros(np.shape(bbox)[0])
        for i in range(np.shape(bbox)[0]):
            area[i]=bbox[i][2]*bbox[i][3]
        I=list(area).index(max(area))
        mask = cv2.inRange(hsv[bbox[I][1]:bbox[I][1]+bbox[I][3],bbox[I][0]:bbox[I][0]+bbox[I][2]],color[0],color[1])
        index_mask=mask>0
    else:
        mask = cv2.inRange(hsv[bbox[0][1]:bbox[0][1]+bbox[0][3],bbox[0][0]:bbox[0][0]+bbox[0][2]],color[0],color[1])
        index_mask=mask>0
    print (np.sum(index_mask))
    return np.sum(index_mask)
            
cam=camera()
time.sleep(1.5)
if __name__ == '__main__':
    while 1:
        a=time.time()
        if incoming==1:
            try:
                img,hsv=cam.img_update()
                cam.detector(img,hsv)
                cam.sending(int(cam.f))
                incoming=0
                print(time.time()-a)
            except:
                print('error')
