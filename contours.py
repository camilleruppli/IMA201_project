#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
#from PIL import Image
import matplotlib.pyplot as plt

#root = "/Users/camilleruppli/Desktop/Telecom/IMA/IMA201/"
root = "/mnt/c/Users/Renata Baptista/Desktop/Image_project/images/"
T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4_5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8_5ansNormale-distension","Rx11ansNormale-sdbronchique"]

for i in range(len(T)):
    im = cv2.imread(T[i]+".jpg")
    print im.shape
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,110,255,0)
    imgray, contours1, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    im1=im.copy()
    im2=im.copy()
    cv2.drawContours(im1, contours1, -1, (255,0,0), 3)
    print len(contours1)
    partReal = 0
    contoursBigger = []
    for c in contours1:
        perimeter = cv2.arcLength(c,True)
        #print perimeter
        if perimeter > 100:
            contoursBigger.append(c)

    cv2.drawContours(im2, contoursBigger, -1, (0,0,0), -1)
    cv2.imwrite("result"+T[i]+".jpg", im2)
    print "Cleaning contours",len(contoursBigger)
    cv2.imwrite("t_contours_"+T[i]+".png",im1)
