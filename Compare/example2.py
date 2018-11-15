import cv2
import numpy as np
from matplotlib import pyplot as plt

import glob
import time
import os

MIN_MATCH_COUNT = 8
no = 10000
big_image = cv2.imread('src/big.jpg',0) 
small_image = cv2.imread('src/small1.jpg',0) 

Matches = []    

orb = cv2.ORB_create()

######## Resize them (they are too big)
# Get their dimensions        
#height, width = big_image.shape[:2]
#         print(heightM, widthM, height, width)        

#big_image = cv2.resize(big_image, (int(width / 4), int(height / 4)),interpolation=cv2.INTER_CUBIC)
###########################


# Find the features
kp1, des1 = orb.detectAndCompute(big_image,None)   # kp are the keypoints, des are the descriptors
kp2, des2 = orb.detectAndCompute(small_image,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(small_image, kp1, big_image, kp2, matches[:10],None, flags=2)
plt.imshow(img3),plt.show()
print('matches', len(matches))
#############

'''
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
'''