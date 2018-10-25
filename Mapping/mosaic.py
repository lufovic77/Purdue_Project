import cv2
import numpy as np

import glob
import time
import os



class Mosaic :

    def __init__(self, ImagePath, Image):

        self.FirstImage = os.path.abspath(Image)
        self.TotalImage = os.path.abspath(ImagePath)
        
        self.first_img = cv2.imread(self.FirstImage)
        self.images = sorted(glob.glob(self.TotalImage))    # for reading images
        
        self.n = 10000   # no of features to extract
        self.MIN_MATCH_COUNT = 8
        
    def warpImages(self, img1, img2, H):

        rows1, cols1 = img1.shape[:2]
        rows2, cols2 = img2.shape[:2]

        list_of_points_1 = np.float32([[0,0], [0,rows1], [cols1,rows1], [cols1,0]]).reshape(-1,1,2)
        temp_points = np.float32([[0,0], [0,rows2], [cols2,rows2], [cols2,0]]).reshape(-1,1,2)
        list_of_points_2 = cv2.perspectiveTransform(temp_points, H)
        list_of_points = np.concatenate((list_of_points_1, list_of_points_2), axis=0)
        

        [x_min, y_min] = np.int32(list_of_points.min(axis=0).ravel() - 0.5)
        [x_max, y_max] = np.int32(list_of_points.max(axis=0).ravel() + 0.5)
        translation_dist = [-x_min,-y_min]
        H_translation = np.array([[1, 0, translation_dist[0]], [0, 1, translation_dist[1]], [0,0,1]])
        
        print("Min and Max:", x_min, y_min, x_max, y_max)
        print("Translation Distance:", translation_dist)    

        self.output_img = cv2.warpPerspective(img2, H_translation.dot(H), (x_max-x_min, y_max-y_min))
        FrameSize = self.output_img.shape
        NewImage = img2.shape
        self.output_img[translation_dist[1]:rows1+translation_dist[1], translation_dist[0]:cols1+translation_dist[0]] = img1
        
        OriginR = int(list_of_points_2[0][0][1])
        OriginC = int(list_of_points_2[0][0][0])
        
        # if the origin of projected image is out of bounds, then mapping to ()
        if OriginR < 0:
            OriginR = 0
        if OriginC < 0:
            OriginC = 0
            
        # Clipping the new image, if it's size is more than the frame    
        if NewImage[0] > FrameSize[0]-OriginR:
            img2 = img2[0:FrameSize[0]-OriginR,:]
            
        if NewImage[1] > FrameSize[1]-OriginC:
            img2 = img2[:,0:FrameSize[1]-OriginC]    
                
        print("Image 2 Magic size:", img2.shape)
        self.output_img[OriginR:NewImage[0]+OriginR, OriginC:NewImage[1]+OriginC] = img2    
        
        return self.output_img

    def giveMosaic(self):
        
        tic = time.clock()

        try:
            if not os.path.exists('result'):
                os.makedirs('result')
        except OSError:
            pass

        EList = []      # this stores the average reprojection error
        ImgList = []          # No of images stitched
        Matches = []    # this stores the number of good matches at every stage
        i = 1
        
        heightM, widthM = self.first_img.shape[:2]
        self.first_img = cv2.resize(self.first_img, (int(widthM / 4), int(heightM / 4)), interpolation=cv2.INTER_CUBIC)
        RecMosaic = self.first_img
        
        for name in self.images[1:]: # except First image
            
            print(name)
            image = cv2.imread(name) 
            
            
            sift = cv2.xfeatures2d.SIFT_create(self.n)
            #sift = cv2.ORB_create(no)
            
            ######## Resize them (they are too big)
            # Get their dimensions        
            height, width = image.shape[:2]
    #         print(heightM, widthM, height, width)        
            
            image = cv2.resize(image, (int(width / 4), int(height / 4)),interpolation=cv2.INTER_CUBIC)
            ###########################


            # Find the features
            kp1, des1 = sift.detectAndCompute(RecMosaic,None)   # kp are the keypoints, des are the descriptors
            kp2, des2 = sift.detectAndCompute(image,None)
            
            ########### FLANN Matcher  ##########      
            FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
            search_params = dict(checks = 50)
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(des1,des2,k=2)
            #############
            
            
            # store all the good matches as per Lowe's ratio test.
            good = []
            allPoints = []
            for m,n in matches:
                if m.distance < 0.7*n.distance:
                    good.append(m)
                    
                allPoints.append(m)
            
            Matches.append(len(good))
            print("Good_Matches:", len(good))
            ##################################
            
            #### Finding the homography #########
            if len(good) >= self.MIN_MATCH_COUNT :
                src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
                dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
                
                #all_src_pts = np.float32([ kp1[m.queryIdx].pt for m in allPoints ]).reshape(-1,1,2)
                #all_dst_pts = np.float32([ kp2[m.trainIdx].pt for m in allPoints ]).reshape(-1,1,2)
                
                M, tmp = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 20.0)

                ###################################
            
                
                #### Finding the euclidean distance error ####
                list1 = np.array(src_pts)    
                list2 = np.array(dst_pts)
                list2 = np.reshape(list2, (len(list2), 2))
                ones = np.ones(len(list1))    
                TestPoints = np.transpose(np.reshape(list1, (len(list1), 2)))
                print("Length:", np.shape(TestPoints), np.shape(ones))
                TestPointsHom = np.vstack((TestPoints, ones))  
                print("Homogenous Points:", np.shape(TestPointsHom))

                if M is None :
                    print("M is none")
                    continue
                print("M", M)
                print("TestPointsHom", TestPointsHom)

                projectedPointsH = np.matmul(M, TestPointsHom)  # projecting the points in test image to collage image using homography matrix    
                projectedPointsNH = np.transpose(np.array([np.true_divide(projectedPointsH[0,:], projectedPointsH[2,:]), np.true_divide(projectedPointsH[1,:], projectedPointsH[2,:])]))
                
                print("list2 shape:", np.shape(list2))
                print("NH Points shape:", np.shape(projectedPointsNH))
                print("Raw Error Vector:", np.shape(np.linalg.norm(projectedPointsNH-list2, axis=1)))
                Error = int(np.sum(np.linalg.norm(projectedPointsNH-list2, axis=1)))
                print("Total Error:", Error)
                AvgError = np.divide(np.array(Error), np.array(len(list1)))
                print("Average Error:", AvgError)
                
                ##################       
                
                i+=1

                RecMosaic = self.warpImages(RecMosaic, image, M)
                cv2.imwrite("result/FinalMosaicTemp.jpg", RecMosaic)
                print(i)
                
                EList.append(AvgError)
                ImgList.append(i)
            else :
                print("Not enough matches are found - %d/%d" % (len(good), self.MIN_MATCH_COUNT))
            if i==40:
                break
            
        
        cv2.imwrite("result/FinalMosaic.jpg", RecMosaic)
        os.remove("result/FinalMosaicTemp.jpg")
        toc = time.clock()
        print(toc-tic)

        return EList, ImgList, Matches

if __name__ == "__main__" :

    mosaic = Mosaic("/Users/choeyujin/Downloads/Original Images/*.JPG","/Users/choeyujin/Downloads/Original Images/DJI_0001.JPG")
    ErrorList, ImgNumbers, GoodMatches = mosaic.giveMosaic()