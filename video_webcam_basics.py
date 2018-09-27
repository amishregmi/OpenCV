--------------------------------------------------------------------------------------------------------------------------------
INTERACTING WITH WEBCAM OR VIDEO FILE
--------------------------------------------------------------------------------------------------------------------------------
cap=cv2.VideoCapture(0) #0 to capture video from first webcam. The whole command returns video from the first webcam. 

while(True):
	ret,frame=cap.read() #ret is boolean for whether or not something was returned. frame is each frame returned. 
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converting each frame to gray.

	cv2.imshow('gray', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

---------------------------------------------------------------------------------------------------------------------------------
TO RECORD AND SAVE THE RECORDING TO A NEW FILE
---------------------------------------------------------------------------------------------------------------------------------

import numpy as np 
import cv2 

cap = cv2.VideoCapture(0)

fourcc= cv2.VideoWriter_fourcc(*'XVID') 
out=cv2.VideoWriter('name.avi', fourcc, 20.0, (640,480)) #Name of video...number of frames per second and the dispaly of the video.

Then within the while loop, we use out.write(frame) to output the frame. and then we do out.release after the while loop. 

fourcc=cv2.VideoWriter_fourcc(*'XVID') #CODEC
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) #Size of file
cap = cv2.VideoCapture(0) #0 as in capturing from the first webcam. To load in a video ifle, VideoCapture('name.extension')

while True:
	ret, frame = cap.read() #True or false and the frame. 
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #ConvertColor of frame . blue green red to gray.
	out.write(frame)
	cv2.imshow('frame',frame) #give name 'frame'. Color frame.
	cv2.imshow('gray', gray)

	if cv2.waitKey(1) & 0xFF==ord('q'): #if q is pressed.
		break

out.release()
cap.release() #Release camera. 
cv2.destroyAllWindows()
