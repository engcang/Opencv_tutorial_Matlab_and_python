#!/usr/bin/env python
"""
Created on Fri Nov  9 10:25:22 2018
@author: mason
"""
'''libraries'''
import time
import numpy as np
import cv2

global LSD
global cap
LSD = cv2.createLineSegmentDetector(0)
cap = cv2.VideoCapture(0)
def keeping(hsv,img):
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

def imageupdate():
    global cap
    ret, image=cap.read()
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    return image,hsv
        
time.sleep(1.2)
if __name__=='__main__':
        try:
            img,hsv=imageupdate()
            cv2.imshow('raw',img)
            cv2.waitKey()
            keeping(hsv,img) 
        except :
            print('got error')
