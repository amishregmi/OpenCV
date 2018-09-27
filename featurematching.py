#Brute-Force Matcher. 

Takes description of one feature in first set and is matched with all other features in second set
The closest one is returned.

We have to created BFMatcher object using cv2.BFMatcher()
Two optional parameters. normType- distance to be used

Second param is crossCheck which is false by default. 

Once created, two important methods are BFMatcher.match() and BFMatcher.knnMatch()

First returns the best match. Second returns k best matches where k is specified by user.

cv2.drawMatches() helps us draw the matches. 
cv2.drawMatchesKnn() draws all the k best matches. 

------------------------------------------------------------------
#Trying to find queryImage in trainImage using feature matching.

import numpy as np 
import cv2
import matplotlib.pyplot as plt 

img1=cv2.imread('box.png') #Query image 
img2= cv2.imread('abc.png') #train image 

#INITIATE DETECTOR 

orb = cv2.ORB()

#find key points and descriptions with SIFT 

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None )

#CREATE BFMATCHER OBJECT 

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) #cv2.NORM_HAMMING since we are using ORB. crossCheck switched on for better results.

matches = bf.match(des1, des2)

#sort them in ascending order of their distances so best matches (with low distance)  can come to front

matches=sorted(matches, key = lambda x: x.distance)

#then we draw only first 10 matches. 

img3= cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], flags = 2)

plt.imshow(img3), plt.show()