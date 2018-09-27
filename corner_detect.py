#Can be used in motion tracking, character recognition, shape recognition etc.

import numpy as np 
import cv2 

img=cv2.imread('abc.png')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray=np.float32(gray) #conver to float 32 to satisfy to algorithm.

corners=cv2.goodFeaturesToTrack(gray, 100,0.01, 10) #image, max corners to detect, quality, and minimum distance between corners. 

corners=np.int0(corners) 

for corner in corners:
	x,y = corner.ravel()
	cv2.circle(img, (x,y), 3, 255, -1) #-1 to fill it in #DRAW CIRCLES FOR CORNERS.

cv2.imshow('Corner', img)

