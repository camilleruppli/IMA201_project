import numpy as np
import cv2
import random as rd
import matplotlib.pyplot as plt

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
    X = []
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
            if(v1[0,0]!=0):
                O1=np.arctan(v1[0,1]/v1[0,0])
            else:
                O1=np.pi/2
            if(v2[0,0]):
                O2=np.arctan(v2[0,1]/v2[0,0])
            else:
                O2=np.pi/2
            X.append(O1)
            X.append(O2)
    print(X)
    bins = np.arange(min(X),max(X), 500)
    plt.hist(X)
    plt.savefig('Orientation/histo_'+T[j]+'.png')
    plt.close()
