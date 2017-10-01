import cv2
import numpy as np

T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4_5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8_5ansNormale-distension","Rx11ansNormale-sdbronchique"]

for i in range(len(T)):
    im=cv2.imread(T[i]+".jpg")
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 120, 255, 0)
    imgray,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Find the index of the largest contour
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt=contours[max_index]

    # Defyning a rectangle that circunscrite the max contour
    im1=im.copy()
    x,y,w,h = cv2.boundingRect(cnt)

    # Defyning the contours of this rectangle and painting the outside in black
    contRect = np.array( [ [x,y], [x,y+h], [x+w, y+h], [x+w,y] ] )
    stencil = np.zeros(im.shape).astype(im.dtype)
    color = [255, 255, 255]
    cv2.fillPoly(stencil, [contRect] , color)
    result = cv2.bitwise_and(im1, stencil)

    cv2.imwrite("boundingBox"+T[i]+".jpg",result) #see partials results

    ##m------------------------------------ SECOND PART
    im=cv2.imread("boundingBox"+T[i]+".jpg", 0)
    ret,thresh = cv2.threshold(im,140,255,0)
    anything,contours,hierarchy = cv2.findContours(thresh, 1, 2)
    im2=im.copy()

    contoursBigger = []
    for c in contours:
        perimeter = cv2.arcLength(c,True)
        #print perimeter
        if perimeter > 100:
            contoursBigger.append(c)
    cv2.drawContours(im2, contoursBigger, -1, (0,0,0), -1)
    cv2.imwrite("2_boundingBox"+T[i]+".jpg",im2) #see partials results

    ##m------------------------------------ THIRD PART
    imDEBUG=cv2.imread("2_boundingBox"+T[i]+".jpg", 0)
    ret,thresh = cv2.threshold(imDEBUG,130,255,0)
    anything,contours,hierarchy = cv2.findContours(thresh, 1, 2)
    im3=imDEBUG.copy()

    # Find the index of the largest contour
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt=contours[max_index]
    #print cnt

    # Defyning a rectangle that circunscrite the max contour
    x,y,w,h = cv2.boundingRect(cnt)
    contRect = np.array( [ [x,y], [x,y+h], [x+w, y+h], [x+w,y] ] )
    stencil = np.zeros(imDEBUG.shape).astype(imDEBUG.dtype)
    color = [255, 255, 255]
    #cv2.fillPoly(stencil, [contRect] , color)
    #result = cv2.bitwise_and(im3, stencil)
    cv2.rectangle(im3,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imwrite("3_boundingBox"+T[i]+".jpg",im3) #see partials results
