#if you have a template and an image, match them.
#The close botton is always the same. so in that case, this could be used...

import cv2
import numpy as np 
#Bigger image 
img_bgr = cv2.imread('temp-match.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

#The image we are searching for in bigger image.
template = cv2.imread('tmplat.jpg')

width, height = template.shape()

result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED) #the last thing is to match
threshold = 0.8 #80%

loc = np.where(res >=threshold) #where in the image the result is greater than threshold

for point in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0 + width], pt[1] + height) , (0, 255,255), 2) #color and width of the rectangle drawn. 

cv2.imshow('detec', img_bgr)

