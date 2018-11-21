import numpy as np
import cv2

def contour_iteration(img, contours) :
    
    max = 0
    val = 0
    for i in range(len(contours)) :
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        if max < area :
            max = area
            val = i

    return val, max

def findContour_child(hierarchy, contours, parent) :
    max = 0
    val = 0
    num = 0
    for hc in hierarchy:
        for h in hc:
            num += 1
            if h[3] == parent :
                cnt = contours[num-1]
                area = cv2.contourArea(cnt)
                if max < area :
                    max = area
                    val = num-1
    return val
    
def contour_draw() :

    origin_img = cv2.imread('path/to/image')

    # sigmaColar == sigmaSpace, the larger the more blur
    solarimg = cv2.bilateralFilter(origin_img, 25, 200, 200)
    solarimg = cv2.cvtColor(solarimg, cv2.COLOR_BGR2GRAY)
    defectimg = solarimg

    _, thr1 = cv2.threshold(solarimg, 210, 255, cv2.THRESH_BINARY)

    thr2 = cv2.adaptiveThreshold(defectimg, 210, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 505, 15)
  
    _, solar_contours, _ = cv2.findContours(thr1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    _, defective_contours, _ = cv2.findContours(thr2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    solar_max, smax = contour_iteration(solarimg, defective_contours)
    defect_max, dmax = contour_iteration(defectimg, solar_contours)
    cv2.drawContours(origin_img, solar_contours, defect_max, (0, 0, 0), 10)
    cv2.drawContours(origin_img, defective_contours, solar_max, (0, 0, 0), 10)
    cv2.imshow('contour', origin_img)
    #cv2.imwrite('/path/to/outimg', origin_img)
    print('defective cell/solar panel : ', (dmax/smax)*100)
    cv2.waitKey(0)


contour_draw()
