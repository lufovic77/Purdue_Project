import numpy as np
import cv2

def contour_iteration(img, contours) :
    
    max = 0
    val = 0
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
    return val

def contour_draw() :

    origin_img = cv2.imread('src/totoro.png')
    #origin_img = cv2.resize(origin_img, (740, 440))

    # sigmaColar == sigmaSpace, the larger the more blur
    grayimg = cv2.bilateralFilter(origin_img, 9, 200, 200)
    grayimg = cv2.cvtColor(grayimg, cv2.COLOR_BGR2GRAY)
    
    #thresh = 35
    #_, thr = cv2.threshold(grayimg, 30, 255, cv2.THRESH_TOZERO)

    #canny_img = cv2.Canny(grayimg, 50, 100, L2gradient=True)
    
    thr = cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 401, 15)
    # blocksize % 2 ==1
    
    _, origin_contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(hierarchy)
    origin_max = contour_iteration(grayimg, origin_contours)
    cv2.drawContours(origin_img, origin_contours, -1, (0, 0, 255), 1)
    cv2.imshow('contour', origin_img)
    cv2.waitKey(0)


contour_draw()