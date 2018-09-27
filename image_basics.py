import cv2
import numpy as np
import matplotlib.pyplot as plt

----------------------------------------------------------------
READING AN IMAGE 
----------------------------------------------------------------

img = cv2.imread('a.png', cv2.IMREAD_GRAYSCALE)

OTHER OPTIONS: IMREAD_COLOR OR LOOK ONLINE FOR OTHERS 

-----------------------------------------------------------------
DISPLAYING AN IMAGE 
-----------------------------------------------------------------
cv2.imshow('Asma', img) 
cv2.waitKey(0) #Wait for any key to be pressed. OR cv2.waitKey(1) && 0xFF==ord('q')
cv2.destroyAllWindows()
------------------------------------------------------------------
PLOTTING IMAGE ON A GRAPH 
-------------------------------------------------------------------
plt.imshow(img, cmap = 'gray' , interpolation='bicubic') #LOOK ONLINE FOR THESE DEFINITIONS AND OTHER POSSIBLE VALUES 
plt.plot([50,100], [80,100], 'c' , linewidth=5)
plt.show()

--------------------------------------------------------------------
SAVING IMAGE 
--------------------------------------------------------------------
cv2.imwrite('abc.png', img) #to save image...





