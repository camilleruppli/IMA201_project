# Telecom Paristech
# IMA201 - 2017/2018
# Projet: detection d'anomalie RX (tuberculose)
#
# Prof: Isabelle Bloch
# 
# etudiants: Camille Ruppli et Renata Baptista
# Part 3/4

import cv2
import numpy as np

T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4_5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8_5ansNormale-distension","Rx11ansNormale-sdbronchique"]

M1=[]
M2=[]
M3=[]

for i in range(len(T)):
    img = cv2.imread('Lungsonly/lungsonly_'+T[i]+'.jpg')
    Z = img.reshape((-1, 3))

        # convert to np.float32
    Z = np.float32(Z)
        # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 4
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        # Now convert back into uint8, and make original image
    center = np.uint8(center)
    V=[]
    for j in range(len(center)):
        V.append(center[j][0])
    V=sorted(V)
    print('V=',V)
    im = cv2.imread('Kmeans/kmeans5/kmeans5_'+T[i]+'.jpg')
    color = ('b','g','r')
    for k,col in enumerate(color):
        histr = cv2.calcHist([im],[k],None,[256],[0,256])
    M1.append(histr[V[1]][0])    #values of the centroids, will be used to see the average values in the histogram
    M2.append(histr[V[2]][0])
    M3.append(histr[V[3]][0])

print('M1=',M1)
print('M2=',M2)
print('M3=',M3)
m1=np.mean(np.array(M1))
m2=np.mean(np.array(M2))
m3=np.mean(np.array(M3))
print('m1=',m1)
print('m2=',m2)
print('m3=',m3)

for i in range(len(M1)):
    if M1[i]>m1:
        print('Image ', i,  'might present an abnormality')
        img=cv2.imread('Kmeans/kmeans5_'+T[i]+'.jpg')
        im=img.copy()

    elif M2[i]>m2:
        print('Image ',i,' might present an abnormality')
    elif M3[i]>m3:
        print('Image ',i,' might present an abnormality')








