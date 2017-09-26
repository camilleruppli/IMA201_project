import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

root = "/Users/camilleruppli/Desktop/Telecom/IMA/IMA201/"
T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4,5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8,5ansNormale-distension","Rx11ansNormale-sdbronchique"]

for i in range(len(T)):
    im = cv2.imread(root+T[i]+'.jpg')
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    imgray, contours1, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    im1=im.copy()
    cv2.drawContours(im1, contours1, -1, (255,0,0), 3)
    cv2.imwrite(root+"contours_"+T[i]+".png",im1)



