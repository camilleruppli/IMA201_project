# Telecom Paristech
# IMA201 - 2017/2018
# Projet: detection d'anomalie RX (tuberculose)
#
# Prof: Isabelle Bloch
# 
# etudiants: Camille Ruppli et Renata Baptista
# Part 4/4

import numpy as np
import cv2
import random as rd
import matplotlib.pyplot as plt

T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4_5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8_5ansNormale-distension","Rx11ansNormale-sdbronchique"]
s=3
for j in range(len(T)):
    im=cv2.imread('Lungsonly/lungsonly_'+T[j]+'.jpg',0)
    im1=im.copy()
    im2=im.copy()
    d2x = cv2.Sobel(im,cv2.CV_64F,2,0,ksize=s) #calcul des dérivées en utilisant un filtre de Sobel convolué par un noyau gaussien de taille s
    d2y = cv2.Sobel(im,cv2.CV_64F,0,2,ksize=s)
    dxy = cv2.Sobel(im,cv2.CV_64F,1,1,ksize=s)
    M=np.matrix('0,0;0,0') #matrice tenseur de structure
    rows = im.shape[1]
    columns = im.shape[0]
    X=[]
    Y=[]
    Z=[]
    for i in range(rows):
        n=rd.randint(0,columns-1)
        if(im[n,i]!=0):
            M[0,0]=d2x[n,i]
            M[0,1]=dxy[n,i]
            M[1,0]=dxy[n,i]
            M[1,1]=d2y[n,i]
            vp=np.linalg.eig(M)
            vp1=vp[0][0] #valeur propre
            vp2=vp[0][1]
            v1=vp[1][0] #vecteur propre
            v2=vp[1][1]
            X.append(vp1)
            Y.append(vp2)
            cv2.line(im1,(i,n),(i+int(20*v1[0,0]),n+int(20*v1[0,1])),(255,0,0),5) #tracer tous les vecteurs propres sans seuil
            cv2.line(im1,(i,n),(i+int(20*v2[0,0]),n+int(20*v2[0,1])),(0,255,0),5)

            if(abs(vp1)>1 or abs(vp2)>1): #on trace le vecteur propre en fonction du rapport des valeurs propres
                m=max(abs(vp1),abs(vp2))
                if(abs(vp2-vp1)/m>0.3):
                    if(m==abs(vp2)):
                        cv2.line(im2, (i, n), (i+int(max(abs(vp1),abs(vp2))*v2[0,0]), n+int(max(abs(vp1),abs(vp2))*v2[0,1])), (255, 0, 0), 5)
                    else:
                        cv2.line(im2, (i, n), (i+int(max(abs(vp1),abs(vp2))*v1[0,0]), n+int(max(abs(vp1),abs(vp2))*v1[0,1])), (255, 0, 0), 5)
    cv2.imwrite('Tensor/'+T[j]+'_tensor2_'+str(s)+'.jpg',im1)
    cv2.imwrite('Tensor/'+T[j]+'_tensor2seuil_'+str(s)+'.jpg',im2)
    m1=np.median(np.array(X))
    m2=np.median(np.array(Y))
    print(m1,m2)
    plt.scatter(X,Y)
    plt.savefig('Tensor/eigen_values_'+T[j]+'.jpg')
    plt.close()





