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
    return val, max

def contour_draw() :

    origin_img = cv2.imread('src/real/80.jpg')
    #origin_img = cv2.resize(origin_img, (740, 440))

    # sigmaColar == sigmaSpace, the larger the more blur
    #grayimg = cv2.bilateralFilter(origin_img, 25, 200, 200)
    grayimg = cv2.bilateralFilter(origin_img, 25, 200, 200)
    grayimg = cv2.cvtColor(grayimg, cv2.COLOR_BGR2GRAY)
    tmpimg = grayimg
    
    #thresh = 35

    #_, thr1 = cv2.threshold(grayimg, 200, 255, cv2.THRESH_BINARY)
    #cv2.imshow('thres', thr1)
    _, thr1 = cv2.threshold(grayimg, 210, 255, cv2.THRESH_BINARY)

    #canny_img = cv2.Canny(grayimg, 50, 100, L2gradient=True)
    
    thr2 = cv2.adaptiveThreshold(tmpimg, 210, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 505, 15)
    #thr2 = cv2.adaptiveThreshold(tmpimg, 100, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 995, 15)
    #_, thr2 = cv2.threshold(tmpimg, 138, 255, cv2.THRESH_BINARY)
    # blocksize % 2 ==1
    
    _, solar_contours, hierarchy = cv2.findContours(thr1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    _, defective_contours, hierarchy = cv2.findContours(thr2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(hierarchy)
    origin_max, max1 = contour_iteration(grayimg, defective_contours)
    origin_max2, max2 = contour_iteration(tmpimg, solar_contours)
    cv2.drawContours(origin_img, solar_contours, origin_max2, (0, 0, 0), 10)
    cv2.drawContours(origin_img, defective_contours, origin_max, (0, 0, 0), 10)
    cv2.imshow('contour', origin_img)
    #cv2.imwrite('src/real/70_result.jpg', origin_img)
    print((max2/max1)*100)
    cv2.waitKey(0)


contour_draw()
