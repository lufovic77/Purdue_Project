import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
'''
from scipy import misc
from scipy.ndimage import gaussian_filter
'''
#/home/kyungmin/Desktop/purdueproject/ColorDetection/src/fluke/FLUKE_GRAY_1.png
#/home/kyungmin/Desktop/purdueproject/ColorDetection/src/fluke/FLUKE_Solar_1.png
def canny():
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
	filepath = "result/"+justName+"_contour.png" #jpg is not supported!!!!
	global srcimg 
	srcimg = cv2.imread(args["image"])
	global grayimg  
	grayimg = cv2.cvtColor(srcimg, cv2.COLOR_BGR2GRAY)

	#canny_img = cv2.Canny(grayimg, 0, 100)
	canny_img = cv2.Canny(srcimg, 0, 70)
	# the third argument for Canny is the threshold value
	retimg, contours, hierarchy = cv2.findContours(canny_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#	cv2.drawContours(retimg, contours, -1, (0,255,0), 3)
#	cv2.drawContours(retimg, contours, 3, (0,255,0), 3)
	cnt = contours[4]

#	for cnt in contours:
#   		x,y,w,h = cv2.boundingRect(cnt)
#   		cv2.rectangle(retimg,(x,y),(x+w,y+h),(200,200,200),2)

# this for loop to make the rectangle for each contour   
	cv2.drawContours(retimg, [cnt], 0, (0,255,0), 3)
	cv2.imshow('contour', retimg)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	plt.savefig(filepath)	# how to save image using ndarray
'''
def gaussian():
	ax1 = grayimg.add_subplot(121)
	ax2 = grayimg.add_subplot(122)
	ascent = misc.ascent()
	result = gaussian_filter(ascent, sigma = 5)
	ax1.imshow(ascent)
	ax2.imshow(result)
	plt.show()
'''
canny()

