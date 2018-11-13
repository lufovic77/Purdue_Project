# contour algorithm
- solar panel detection 
    - apply noise to image : cv2.bilateralFilter()
    - apply grayscale to image : cv2.cvtColor()
    - set threshold : cv2.adaptiveThreshold()
    - find contour, hierarchy : cv2.findContours()
    - call contour_iteration() and find max area
        - find each contour area using iteration : cv2.contourArea()
    - draw contour into image : cv2.drawContours()