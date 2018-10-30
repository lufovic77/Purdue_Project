'''
From: http://creativemorphometrics.co.vu/blog/2014/08/05/automated-outlines-with-opencv-in-python/
Modified: Joey Kim (lufovic77@gmail.com)
'''
import numpy as np
import cv2
import argparse
from matplotlib import pyplot as plt 


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", help = "it means path to images")
#option: i, key: image, help: option
args = vars(parser.parse_args())

#parsing the args
mystring = str(args["image"])
mylist = mystring.split("/")
index = len(mylist)
namewithformat = mylist[index-1] #like "solar.jpg"
name = namewithformat.split(".")
justName = name[0] #like "solar"

#load images from disk 
gwash = cv2.imread(args["image"])
gwashBW = cv2.cvtColor(gwash, cv2.COLOR_BGR2GRAY)

plt.imshow(gwashBW, 'gray')	
#plt.savefig(filename)	# how to save image using ndarray
plt.xticks([]), plt.yticks([])
plt.show() #shows the gray scale of pic

#cv2.imshow('gwash', gwashBW) #Also supports conversion to the gray scale
#cv2.waitKey(0)

'''
ret, thresh1 = cv2.threshold(gwashBW, 150, 255, cv2.THRESH_BINARY)
#Parameters: (grayscale img src, threshold, applied value when exceeds the threshold, thresholding type)
#WHITE when bigger than the threshold
#BLACK when smaller than the threshold
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(thresh1, kernel,iterations = 1)

opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)


plt.imshow(closing, 'gray')
plt.xticks([]), plt.yticks([])
plt.show()
'''
'''
contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find contours with simple approximation

cv2.imshow('cleaner', closing) #Figure 3
cv2.drawContours(closing, contours, -1, (255, 255, 255), 4)
cv2.waitKey(0)
'''