import cv2
import numpy as np

srcimg = cv2.imread('src/image.png')
srcimg =  cv2.resize(srcimg, (700,400))
#srcimg = cv2.GaussianBlur(srcimg, (5,5), 0)

#bilateralFilter first parameter 클수록 끊어짐
grayimg = cv2.bilateralFilter(srcimg, 35, 500, 200)
grayimg = cv2.cvtColor(grayimg, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', grayimg)
cv2.waitKey(0)

thresh = 23

thrs = cv2.getTrackbarPos('thrs', 'edge')
#thrs = -1

canny_img = cv2.Canny(grayimg, thresh, thrs, apertureSize=3, L2gradient=True)
#mask = cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,1)
_,mask = cv2.threshold(grayimg,100,5,cv2.THRESH_BINARY)
''' 

erodeSize = 5
dilateSize = 7
eroded = cv2.erode(mask, np.ones((erodeSize, erodeSize)))
mask = cv2.dilate(eroded, np.ones((dilateSize, dilateSize)))
'''
#cv2.imshow('canny', canny_img)

#cv2.imshow("preview", cv2.resize(cv2.cvtColor(mask*canny_img, cv2.COLOR_GRAY2RGB) | srcimg, (640, 480), interpolation = cv2.INTER_CUBIC))
#cv2.waitKey(0)
cv2.imshow('canny', canny_img)
cv2.waitKey(0)
cv2.imshow('canny*mask', canny_img*mask)
cv2.waitKey(0)
retimg, contours, hierarchy = cv2.findContours(canny_img*mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)) :
    cnt = contours[i]
    cv2.drawContours(srcimg, [cnt], 0, (255, 255, 0), 1)
    cv2.imshow('contour', srcimg)
    cv2.waitKey(0)
'''
for i in range(len(contours)) :
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    print('contour 면적 : ', area)
    print('contour 길이 : ', perimeter)
    if max < area :
        max = area
        val = i

print(max, val)
'''
'''
cv2.drawContours(srcimg, contours, -1, (0, 255, 0), 3)

cv2.imshow('contour', srcimg)
cv2.waitKey(0)
'''