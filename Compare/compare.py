import numpy as np
import cv2

def contour_iteration(img, contours) :
    
    max = 0
    val = 0
    for i in range(len(contours)) :
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if max < area :
            max = area
            val = i

    return val

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

def contour_draw(imgpath, noise=False, params='0') :

    img = cv2.imread(imgpath)
    if noise == True :
        img = cv2.bilateralFilter(img, 10, 20, 20)
        #img= cv2.medianBlur(img,9)
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    if noise == False :
        _, thr = cv2.threshold(grayimg, 135, 200, cv2.THRESH_BINARY)
    elif noise == True :
        _, thr = cv2.threshold(grayimg, 115, 200, cv2.THRESH_BINARY)

    _, contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    max = contour_iteration(grayimg, contours)
    child = findContour_child(hierarchy, contours, max) 

    cv2.drawContours(grayimg, contours, child, (0, 0, 255), 1)
    cv2.imshow('contour', grayimg)
    filename = 'result'+params+'.png'
    cv2.imwrite(filename, grayimg)
    cv2.waitKey(0)
    return contours[child]


cnt1 = contour_draw('/Users/choeyujin/Project/code/Compare/src/b.png', True, '1')
cnt2 = contour_draw('/Users/choeyujin/Project/code/Compare/src/s.png', False, '2')
print(cv2.matchShapes(cnt1, cnt2, 1, 0.0))
