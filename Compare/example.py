import cv2
import numpy as np
from matplotlib import pyplot as plt

import glob
import time
import os

MIN_MATCH_COUNT = 8
no = 10000
big_image = cv2.imread('src/big.jpg') 
small_image = cv2.imread('src/small1.jpg') 

Matches = []    

sift = cv2.xfeatures2d.SIFT_create(10000)
#sift = cv2.ORB_create(no)

######## Resize them (they are too big)
# Get their dimensions        
height, width = big_image.shape[:2]
#         print(heightM, widthM, height, width)        

big_image = cv2.resize(big_image, (int(width / 4), int(height / 4)),interpolation=cv2.INTER_CUBIC)
###########################


# Find the features
kp1, des1 = sift.detectAndCompute(small_image,None)   # kp are the keypoints, des are the descriptors
kp2, des2 = sift.detectAndCompute(big_image,None)

########### FLANN Matcher  ##########      
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1,des2,k=2)

#img3 = cv2.drawMatches(big_image,kp2, small_image, kp1, matches[:10], flag=2)
#plt.imshow(img3).plt.show()
print('matches', len(matches))
#############


# store all the good matches as per Lowe's ratio test.
good = []
allPoints = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)
        
    allPoints.append(m)

Matches.append(len(good))
print("Good_Matches:", len(good))
##################################