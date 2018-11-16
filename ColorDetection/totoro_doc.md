# contour algorithm
- solar panel detection 
    - apply noise to image : cv2.bilateralFilter()
    - apply grayscale to image : cv2.cvtColor()
    - set threshold : cv2.threshold()
    - find contour, hierarchy : cv2.findContours()
    - draw contour into image : cv2.drawContours()