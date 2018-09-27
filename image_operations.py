import cv2
import numpy 

img= cv2.imread('img.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Original', img)
imgingray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', imgingray)

THRESHOLDING: IF the pixel value is greater than a certain value, assign a value otherwise assign another value.
THE SOURCE IMAGE SHOULD BE GRAYSCALE. 
FIRST ARGUMENT IS SOURCE IMAGE, SECOND IS THRESHOLD VALUE, THIRD IS MaxVal.
RETURNS two values. First is ret, second is the thresholded image. 


------------------------------------------------------------------------------
BINARY THRESHOLDING
------------------------------------------------------------------------------
#cv2.THRESH_BINARY if (x,y) > thresh, give maxval otherwise give 0
#cv2.THRESH_BINARY_INV if (x,y)>thresh, give 0 otherwise give maximum.


-----------------------------------------------------------------------------
SYNTAX
------------------------------------------------------------------------------
ret, thresh = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)


------------------------------------------------------------------------------
ADAPTIVE THRESHOLDING FOR LOW LIGHT IMAGES
------------------------------------------------------------------------------

th=cv2.adaptiveThreshold(grayimage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,1)

#(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[,dist])

------------------------------------------------------------------------------
IMPOSING ONE IMAGE ON ANOTHER 
------------------------------------------------------------------------------

rows,cols,channels=img2.shape #img2 is the smaller image to be imposed

roi = img1[0:rows, 0:cols]

img2gray=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) #Binary threshold, either 0 or 1.

#IF pixel value is greater than threshold value, it is assigned one value, otherwise another. 
#First argument is source image which should be greyscale, second is threshold value pixels, 
#third is maxval which is the value to be given if pixel is more or sometimes less than threshold.

#Thresh binary. if source(x,y) > thresh, give maxval otherwise give 0
cv2.imshow('abc', mask)

mask_inv = cv2.bitwise_not(mask) #The black area of mask. #Logical operation. 

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

img2_foreground= cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_foreground)

img1[0:rows, 0:cols ] = dst 

cv2.imshow('res', img1)

#WE took our original image. WE threshold image for background black and image white and we inversed it to logo black background white. To the smaller image's background, we add the bigger image where logo isn't present.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#PROPER CODE

import cv2
import numpy as np

img1=cv2.imread('bigger.png')
img2=cv2.imread('smaller.png')

rows,cols,channels=smaller.shape #number of rows of image, number of cols and if colored, number of channels.

roi=img1[0:rows, 0:cols]

img2gray=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) #logo is white and background is black.

mask_inv = cv2.bitwise_not(mask) #logo is black and background of logo is white.

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv) #black out area of logo in ROI. 

img2_foreground= cv2.bitwise_and(img2, img2, mask=mask) #take only region of logo from logo image.

dst = cv2.add(img1_bg, img2_foreground)

img1[0:rows, 0:cols ] = dst 

cv2.imshow('res', img1)











img1 =cv2.imread('anotherimage.png')



