# Telecom Paristech
# IMA201 - 2017/2018
# Projet: detection d'anomalie RX (tuberculose)
#
# Prof: Isabelle Bloch
# 
# etudiants: Camille Ruppli et Renata Baptista
# Part 1/4

import cv2
import numpy as np

T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4_5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8_5ansNormale-distension","Rx11ansNormale-sdbronchique"]

for i in range(len(T)):
    im=cv2.imread('images/'+T[i]+'.jpg', 0)
    limit = 120
    ret, thresh = cv2.threshold(im, limit, 255, 0)
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

    cv2.imwrite("boundingBox/boundingBox"+T[i]+".jpg",result) #see partials results

    ##m------------------------------------ SECOND PART

    im=cv2.imread("boundingBox/boundingBox"+T[i]+".jpg",0)
    rows=im.shape[0]
    columns=im.shape[1]
    numbers=np.linspace(0,columns-1,columns)
    S=[]
    for j in range(0,columns):
        V=[]
        for k in range(rows):
            V.append(im[k,j])
        S.append(sum(V))
    print "Cumsum box", sum(S)
    if (sum(S) > 300000000):
        print "images #",i
        limit = 123
        ret, thresh = cv2.threshold(im, limit, 255, 0)
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
        cv2.imwrite("boundingBox/boundingBox"+T[i]+".jpg",result)

    # -- THIRD PART
	# Seuil très strict en considerant deux types des images, clair/sain et lesquels avec le maladie
    im=cv2.imread("boundingBox/boundingBox"+T[i]+".jpg",0)

    im2=cv2.imread("imagesBlack/blackImages"+T[i]+".jpg",0)
    rows=im2.shape[0]
    columns=im2.shape[1]
    numbers=np.linspace(0,columns-1,columns)
    
	# Calcule the sum cummulate
	S=[] 
	for j in range(0,columns):
        V=[]
        for k in range(rows):
            V.append(im2[k,j])
        S.append(sum(V))
    threshold=0
    m=np.median(np.array(S))
    for k in range(len(S)):
        if(S[k]>m/1.5): #compare le sum avec un seuil
            threshold=k
    im1=im.copy()
	
	#put in black the parts above this threshold
    for l in range(threshold,rows):
        im1[l:]=0

    Scol=[]
    for j in range(0,rows):
        V=[]
        for k in range(columns):
            V.append(im2[j,k])
        Scol.append(sum(V))
    cv2.imwrite('Lungsonly/lungsonly_'+T[i]+'.jpg', im1)
