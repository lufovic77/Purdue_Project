# contour algorithm
- solar panel detection 
    - apply noise to image : cv2.bilateralFilter()
    - apply grayscale to image : cv2.cvtColor()
    - set threshold : cv2.threshold() / cv2.adaptiveThreshold()
    - find contour, hierarchy : cv2.findContours()
    - find the largest contour area in hierarchy : cv2.contourArea()
    - draw contour into image : cv2.drawContours()