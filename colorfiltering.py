import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read() #_ is any return value you don't read
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	#HSV color -> IN RGB all three are color values. In HSV, Hue is the color value, Value is 
	#the amount of presence? and Saturation is the intensity. 
	#We modify hue to see how it works for us.

	#Play around with the values to get the best result.

	#Find an item with a unique color. In this case, it was a red hat.

	lower_red = np.array([150,150,50])
	upper_red = np.array([180,255,150])

#Everything is in this range initially. Mask currently looks identical to frame.

	mask=cv2.inRange(hsv, lower_red, upper_red)  #true or false. if in range, it's 1 otherwise 0.
	res = cv2.bitwise_and(frame, frame, mask=mask) 

	#Where? Applied to the frame where frame is equal to frame and mask = mask.
	#IF mask is inRange, we get 1. So for res, it becomes true and we will show color in the frame.

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)

	k = cv2.waitKey(5) & 0xFF #Waitkey used to introduce delay of n milliseconds while rendering images to windows. It on a loop, displays frame by frame. WaitKey(0) displays infinitely until a key is pressed.
	if k == 11:
		break

cv2.destroyAllWindows()
cap.release()









