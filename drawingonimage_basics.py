import numpy as np
import cv2

img= cv2.imread('a.png', cv2.IMREAD_COLOR) #read it in as color

cv2.line(img, (0,0), (150,150), (255,255,255), 15) #where line starts and ends and color of line (blue,green,red), line width = 15 px
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5) #where rectangle starts and ends
cv2.circle(img, (100,63), 55,(0,0,255), -1) #-1 will fill in the image with the color. center , radius, color,  
#Polygon. Will connect points and optionally close polygon.

pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32) #datatype
pts=pts.reshape((-1,1,2))  #opencv documentation suggests to convert array to 1x2

cv2.polylines(img, [pts], True, (0,255,255), 3 ) #TRue is whether or not we want to connect final point to first point...color, line-width

#now...writing.
#FONT
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV TUTS!', (0,130), font, 10, (200,255,255), 2, cv2.LINE_AA) #starting, font, size
#color, thickness.., 


cv2.imshow('image', img)
cv2.waitKey(0) #for any key to be pressed
cv2.destroyAllWindows()