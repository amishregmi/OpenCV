import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read() #_ is any return value you don't read
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	HSV color -> IN RGB all three are color values. In HSV, Hue is the color value, Value is 
	the amount of presence? and Saturation is the intensity. 
	We modify hue to see how it works for us.

	Play around with the values to get the best result.

	Find an item with a unique color. In this case, it was a red hat.

	lower_red = np.array([150,150,50])
	upper_red = np.array([180,255,150])

#Everything is in this range initially. Mask currently looks identical to frame.

	mask=cv2.inRange(hsv, lower_red, upper_red)  #true or false. if in range, it's 1 otherwise 0.
	res = cv2.bitwise_and(frame, frame, mask=mask) 

	#Where? Applied to the frame where frame is equal to frame and mask = mask.
	#IF mask is inRange, we get 1. So for res, it becomes true and we will show color in the frame.


-------------------------------------------------------------------------------------------------------
BLUR BY AVERAGING PICTURES
-------------------------------------------------------------------------------------------------------
kernel = np.ones((15,15), np.float32)/225  $Average of 15x15 pixels 
smoothed = cv2.filter2D(res, -1, kernel) #Apply an average of the frame. #Helps lose background noise but also lose clarity.


----------------------------------------------------------------------------------------------------------
GAUSSIAN BLUR
-----------------------------------------------------------------------------------------------------------
blur = cv2.GaussianBlur(res, (15,15), 0) #image, width and height of kernel, standard deviation in X and Y direction. More clear than average.

MEDIAN BLUR 

median=cv2.medianBlur(res, 15) #15 of size. 






	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)

	k = cv2.waitKey(5) & 0xFF #Waitkey used to introduce delay of n milliseconds while rendering images to windows. It on a loop, displays frame by frame. WaitKey(0) displays infinitely until a key is pressed.
	if k == 11:
		break

cv2.destroyAllWindows()
cap.release()





------------------------------------------------------------------------------------------------------------------------------------
MORPHOLOGICAL TRANSFORMATIONS
------------------------------------------------------------------------------------------------------------------------------------
1) Erosion - Creates a slider that goes around. If any of  the pixels in the slider isn't the same as the other colors, it takes it out.' If identical, it moves on. 
2) Dilation - opposite. Instead of taking it out, it pushes out until it can't be pushed out further. '
3) Opening - remove false positives -> noises in the background. 
4) Closing - remove false negatives.  -> noises in the required image. 
5) Tophat - difference between input image and opening of image 
6) Blackhat - difference between closing. 

kernel = np.ones((5,5), np.unit8) # 5 by 5

erosion = cv2.erode(mask, kernel, iterations = 1)
dilation = cv2.dilate(mask, kernel, iterations=1)
cv2.imshow('abc', erosion) # or cv2.imshow('abc', dilation)

The above methods aren't THAT EFFECTIVE. '

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

cv2.imshow('abc', opening)


-------------------------------------------------------------------------------------------------------------------------------------------










