import numpy as np 
import cv2 

img=cv2.imread('a.png', cv2.IMREAD_COLOR) 

--------------------------------------------------------------------------------------
REFERENCE PIXEL
--------------------------------------------------------------------------------------
px = img[55,55]
print(px) #-> [30 30 42 ] -> Color value for that pixel
img[55,55] = [255,255,255]  #Can modify pixel.

---------------------------------------------------------------------------------------
REGION OF IMAGE 
---------------------------------------------------------------------------------------
roi  = img [100:150, 100:150] 
img[100:150] = [255,255,255]
print(roi)

img[0:74, 0:97] = img[37:111, 20:200]


---------------------------------------------------------------------------------------
ADDING IMAGES. MUST BE THE SAME SIZE. NOT IDEAL.

img1= cv2.imread('...')
img2 = cv2.imread('...')
add= img1+ img2 #both images maintain their opaqueness.

#OR
add = cv2.add(img1, img2) #ADDS ALL THE PIXEL VALUES TOGETHER!!

#OR
weighted=cv2.addWeighted(img, 0.6, img2, 0.4, 0) img1 is 60% img 2 is 40% the last 0 is gamma value leave alone.


