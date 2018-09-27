#BACKGROUND REDUCTION!

#Analyze changes from previous frame. That is the foreground. The things that don't change are the background. ' 

#Works well with finding motions.
import cv2
cap = cv2.VideoCapture('samplevid.mp4')

#fore ground , background

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame)
	cv2.imshow('original', frame)
	cv2.imshow('fg', fgmask)

	k= cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()


