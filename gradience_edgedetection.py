import cv2
import numpy as np 

cap=cv2.VideoCapture(0)

while True:
	_, frame= cap.read()

	laplacian = cv2.Laplacian(frame, cv2.CV_64F) #kinda cool

	cv2.imshow('original', frame)
	cv2.imshow('lap', laplacian)

	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
	cv2.imshow('sobel', sobelx)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)

	#NOW EDGE DETECTION.

	edges = cv2.Canny(frame, 100, 200)
	cv2.imshow('edges', edges)





	if cv2.waitKey(1) & 0xFF==ord('q'):
		break



cv2.destroyAllWindows()
cap.release()

