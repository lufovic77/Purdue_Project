import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('src/big.jpg')          # queryImage
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
_, thr1 = cv2.threshold(img1, 10, 50, cv2.THRESH_TOZERO)

img2 = cv2.imread('src/small1.jpg') # trainImage
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
_, thr2 = cv2.threshold(img2, 10, 50, cv2.THRESH_TOZERO)

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create(10000)

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(thr1,None)
kp2, des2 = sift.detectAndCompute(thr2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

print(len(matches), len(good))
# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(thr1,kp1,thr2,kp2,good,None, flags=2)

plt.imshow(img3),plt.show()
