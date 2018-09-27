'''

1) Collect background images - Get thousands of images where our object isn't present.'
2) Positive - thousands of images of our object. Can make this based on one image or manually create them. Ideally have double the amount of positive images. 
3) Create a vector file by stiching together all positives. Done with opencv command 
4) Train cascade with positives vs negatives.

Negative and positive images need descriptior files. 

Negatives -> Genereally a bg.txt file that containst the path to each image, by line. example line: neg/1.jpg

Positives => pos.txt pos/1,jpg 1 0 0 50 50 -> image, number of objects, start point, rectangle coordinates. 

We want negative images larger than positives. Try to use 100x100 for negatives, 50x50 positives. 

image-net.org to get images. 

Download all URLS of analog watchs. 

OR get one positive, when you need a specific kind of watch for example, and use opencv_createsamples to create many by superimposing on the negatives in various angles and stuff.

Getting negative image from ImageNet. 

First we want to resize All THE IMAGES TO THE SAME SIZE AND SAVE THEM. 

'''

import urllib.request 
import cv2
import numpy as np 
import os 

#WE're going to all links. Download image. Open in OpenCV. Resize and convert to gray and save the image. 

def store_raw_images():
	neg_images_link = ' ...'
	neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

	if not os.path.exists('neg'):
		os.makedirs('neg')

	pick_num =1 

	for i in neg_image_urls.split('\n'):

		try:
			print(i)
			urllib.request.urlretrieve(i, "neg/"+str(pick_num)+ '.jpg')
			img = cv2.imread("neg/"+str(pick_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
			resized_image = cv2.resize(img, (100,100))
			cv2.imwrite("neg/"+str(pick_num)+'.jpg',resized_image)
			pic_num+=1


		except Exception as e:
			print(str(e))

#store_raw_images()

#After completing, run URL of other negative samples but update pic_num. 

#UGLY IMAGE. Wrong image with text. 

#New directory in main directory called uglies. 

def find_uglies():
    match = False
    for file_type in ['neg']: #or ['neg', 'pos']
        for img in os.listdir(file_type): #iterate through all images 
            for ugly in os.listdir('uglies'): #one of the uglies manually copied.
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

#Descriptor file for negative images.

def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n' #number of objects in image, rectangular location.
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)


#google opencv create sample for windows/ Then create a vector file to stich together all positive images. 