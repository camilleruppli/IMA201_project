import cv2
import numpy as np

T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4,5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8,5ansNormale-distension","Rx11ansNormale-sdbronchique"]

for i in range(len(T)):
    im=cv2.imread(T[i]+'.jpg')
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    imgray,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Find the index of the largest contour
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt=contours[max_index]
    im1=im.copy()
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(im1,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imwrite('boundingBox'+T[i]+'.jpg',im1)









