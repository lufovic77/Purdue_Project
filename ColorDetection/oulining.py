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
srcimg = cv2.imread(args["image"])
grayimg = cv2.cvtColor(srcimg, cv2.COLOR_BGR2GRAY)

filepath = "result/"+justName+"_grayscale.png" #jpg is not supported!!!!
plt.imshow(grayimg, 'gray')	
plt.xticks([]), plt.yticks([])
plt.savefig(filepath)	# how to save image using ndarray

#cv2.imshow('gwash', gwashBW) #Also supports conversion to the gray scale
#cv2.waitKey(0)

ret, thresh = cv2.threshold(grayimg, 120, 255, cv2.THRESH_BINARY)
#Parameters: (grayscale img src, threshold, applied value when exceeds the threshold, thresholding type)
#WHITE when bigger than the threshold
#BLACK when smaller than the threshold

retimg, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#several parameters: 1)src image, 2)contour retrieval mode, 3)contour approximation method 
#output: 1)modified image, 2)contours(list of all contours), 3)hierarchy

cnt = contours[4]
cv2.drawContours(retimg, [cnt], 0, (0, 255, 0), 3)
cv2.imshow("result", retimg)
cv2.waitKey(0)

'''
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(thresh1, kernel,iterations = 1)

opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

plt.imshow(closing, 'gray')
plt.xticks([]), plt.yticks([])
plt.show()


contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find contours with simple approximation

'''