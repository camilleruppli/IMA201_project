import numpy as np
import cv2
import random as rd

T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4_5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8_5ansNormale-distension","Rx11ansNormale-sdbronchique"]

for j in range(len(T)):
    im=cv2.imread('Lungsonly/lungsonly_'+T[j]+'.jpg',0)
    im1=im.copy()
    d2x = cv2.Sobel(im,cv2.CV_64F,2,0,ksize=5) #second derivative of x
    d2y = cv2.Sobel(im,cv2.CV_64F,0,2,ksize=5) #second derivative of y
    dxy = cv2.Sobel(im,cv2.CV_64F,1,1,ksize=5) #derivative of x than y
    M=np.matrix('0,0;0,0') #tensor matrix
    rows = im.shape[1]
    columns = im.shape[0]
    for i in range(rows):
        n=rd.randint(0,columns-1)
        if(im[n,i]!=0):
            M[0,0]=d2x[n,i]
            M[0,1]=dxy[n,i]
            M[1,0]=dxy[n,i]
            M[1,1]=d2y[n,i]
            vp=np.linalg.eig(M)
            v1=vp[1][0]
            v2=vp[1][1]
            cv2.line(im1, (i, n), (i+int(20*v1[0,0]), n+int(20*v1[0,1])), (255, 0, 0), 5)
            cv2.line(im1, (i, n), (i+int(20*v2[0,0]), n+int(20*v2[0,1])), (0, 255, 0), 5)
            cv2.imwrite('Tensor/'+T[j]+'_tensor.jpg',im1)



