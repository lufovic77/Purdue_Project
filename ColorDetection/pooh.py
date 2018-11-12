import cv2
import numpy

srcimg = cv2.imread('src/color_origin.jpg')
#srcimg = cv2.GaussianBlur(srcimg, (5,5), 0)
srcimg = cv2.bilateralFilter(srcimg, 9, 100, 100)

thresh = 40
grayimg = cv2.cvtColor(srcimg, cv2.COLOR_BGR2GRAY)

canny_img = cv2.Canny(grayimg, 0, thresh*2, L2gradient=True)
cv2.imshow('canny', canny_img)
cv2.waitKey(0)

retimg, contours, hierarchy = cv2.findContours(canny_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(srcimg, contours, -1, (0, 0, 255), 1)

cv2.imshow('contour', srcimg)
cv2.waitKey(0)