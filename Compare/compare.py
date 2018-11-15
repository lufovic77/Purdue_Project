import numpy as np
import cv2

def contour_iteration(img, contours) :
    
    max = 0
    val = 0
    for i in range(len(contours)) :
        cnt = contours[i]
        '''
        cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)
        cv2.imshow('contour', img)
        cv2.waitKey(0)
        '''
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        print('contour 면적 : ', area)
        print('contour 길이 : ', perimeter)
        if max < area :
            max = area
            val = i
   
    print(max, val)
    return val

def findContour_child(hierarchy, contours, parent) :
    max = 0
    val = 0
    num = 0
    for hc in hierarchy:
        for h in hc:
            num += 1
            if h[3] == parent :
                print('num', num, num-1)
                cnt = contours[num-1]
                area = cv2.contourArea(cnt)
                perimeter = cv2.arcLength(cnt, True)
                print('contour 면적 : ', area)
                print('contour 길이 : ', perimeter)
                if max < area :
                    max = area
                    val = num-1
    return val

def contour_draw(imgpath) :

    img = cv2.imread(imgpath)
    grayimg = cv2.bilateralFilter(img, 5, 100, 100)
    grayimg = cv2.cvtColor(grayimg, cv2.COLOR_BGR2GRAY)
    
    _, thr = cv2.threshold(grayimg, 115, 200, cv2.THRESH_BINARY)

    _, contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    max = contour_iteration(grayimg, contours)
    child = findContour_child(hierarchy, contours, max) 

    cv2.drawContours(grayimg, contours, child, (0, 0, 255), 1)
    cv2.imshow('contour', grayimg)
    cv2.waitKey(0)
    #print('final value', contours[child])
    return contours[child]


cnt1 = contour_draw('/Users/choeyujin/Project/code/Compare/src/b.png')
cnt2 = contour_draw('/Users/choeyujin/Project/code/Compare/src/s.png')
print(cv2.matchShapes(cnt1, cnt2, 1, 0.0))
print(cv2.matchShapes(cnt1, cnt2, 2, 0.0))
print(cv2.matchShapes(cnt1, cnt2, 3, 0.0))