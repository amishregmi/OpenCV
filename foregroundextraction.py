Draw a rectangle around the foreground region. Foreground region should be completely inside the rectangle. Then the algorithm works to get the best result.
We define a rectangle. WE define white stroks for foreground and black strokes for background. and we get a better result .

User inputs rectangle. Everything outside the rectangle is taken as sure background. Everything inside is uknown. Any hard labeling of foreground and background won't change.

DEMO:

img - input image 
mask - mask image specifying which areas are background, foreground, or probable foreground. 
bdgModel, fdgModel = Arrays used by algorithm internally. Should create two np.float64 type zero arrays. 

iterCount = number of iterations algorithm should run .

mode - cv2.GC_INIT_WITH_RECT OR cv2.GC_INIT_WITH_MASK which decides whether we are drawing rectangle or final touchup strokes. 

##FIRST TRY:

import numpy as np 
import cv2
from matplotlib import pyplot as plt 

img=cv2.imread('messi.jpt')
mask= np.zeroes(img.shape[:2], np.uint8)

bdgModel = np.zeroes((1,65), np.float64)
fdgModel= np.zeroes((1,65), np.float64)

rect = (50, 50, 450, 290)

cv2.grabCut(img, mask, rect, bdgModel, fdgModel, 5, cv2.GC_INIT_WITH_RECT) #run for 5 iterations 

#This modifies the mask image. In the new mask image, pixels will be marked with 4 flags denoting foreground/background. 
#We modify mask such that all 0 and 2 pixels are put to 0 (background) and 1 and 3 pixels are put to 1 (foreground)

mask2=np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

#now multiply with our image to get it 

img = img *mask2 [:,:, np.newaxis]

plt.imshow(img)

--------------------------------------------------------------------------------------------------------------------------------

MESSIS HAIR IS GONE IN THE METHOD ABOVE.

We modify the mask as required. 

Go to paint and add white and black. 

newmask = cv2.imread('newmask.png')

#wherever it is white, change mask = 1 (foreground)
#wherever it is  black, change mask = 0 

mask[newmask  ==0] =0 
mask[newmask ==255] = 1

mask, bgmodel, fdgModel = cv2.grabCut(img, mask, None, bgmodel, fdgModel, 5 , cv2.GC_INIT_WITH_MASK)

mask = np.where((masl==2) | (mask ==0) , 0,1).astype('uint8')

img=img*mask[:,:,np.newaxis]
plt.imshow()

