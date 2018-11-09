import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
'''
from scipy import misc
from scipy.ndimage import gaussian_filter
'''

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

	canny_img = cv2.Canny(grayimg, 0, 113)
	cv2.imshow('contour1', canny_img)
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

