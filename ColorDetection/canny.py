import numpy as np
import cv2
import argparse
import matplotlib.pyplot as pyplot
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
	srcimg = cv2.imread(args["image"])
	grayimg = cv2.cvtColor(srcimg, cv2.COLOR_BGR2GRAY)

	canny_img = cv2.Canny(grayimg, 0, 45)
	cv2.imshow('contour1', canny_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

canny()