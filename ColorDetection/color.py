import numpy as np
import argparse
import cv2
#Essential packages 

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", help = "it means path to images")
#option: i, key: image, help: option
args = vars(parser.parse_args())

#load images from disk 
image = cv2.imread(args["image"])

# the list of boundaries -> for RGB colors(order no matters) 
boundaries = [
	([0, 0, 255], [1, 2, 255])	#BGR
]
# it represents the upper limit and lower limit. 
# For the first row of array, it means that 
# one color should be in range of 17 and 50. 
# another color should be in 15 and 56 range
# the other one should be between 100 and 200. 

# Now, use inRange method to implement color detection. 
for (lower, upper) in boundaries:
	lower = np.array(lower, dtype = "uint8") #dtype for datatype
	upper = np.array(upper, dtype = "uint8")

	mask = cv2.inRange(image, lower, upper)
	#image: where the color detection will be performed 
	# lower & upper: the upper and lower limit value of the color 
	output = cv2.bitwise_and(image, image, mask = mask)
	# shows only pixels that corresponds to the mask 

	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
