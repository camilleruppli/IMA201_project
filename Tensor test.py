import numpy as np
import cv2
import random as rd

im=cv2.imread('Rx3ansFoyerInfGauche.jpg',0)
im1=im.copy()
d2x = cv2.Sobel(im,cv2.CV_64F,2,0,ksize=5) #second derivative of x
d2y = cv2.Sobel(im,cv2.CV_64F,0,2,ksize=5) #second derivative of y
dxy = cv2.Sobel(im,cv2.CV_64F,1,1,ksize=5) #derivative of x than y
M=np.matrix('0,0;0,0')
rows = im.shape[1]
columns = im.shape[0]
for i in range(rows):
    n=rd.randint(0,columns-1)
    M[0,0]=d2x[n,i]
    M[0,1]=dxy[n,i]
    M[1,0]=dxy[n,i]
    M[1,1]=d2y[n,i]
    vp=np.linalg.eig(M)
    v1=vp[1][0]
    v2=vp[1][1]
    if(v1[0,0] and v1[0,1] !=0):
        cv2.line(im1, (i, n), (i+1000*int(v1[0,0]), n+1000*int(v1[0,1])), (255, 0, 0), 5)
    if(v2[0,0] and v2[0,1] !=0):
        cv2.line(im1, (i, n), (i+1000*int(v2[0,0]), n+1000*int(v2[0,1])), (0, 255, 0), 5)
    cv2.imwrite('Rx3ansFoyerInfGauche_tensor.jpg',im1)



