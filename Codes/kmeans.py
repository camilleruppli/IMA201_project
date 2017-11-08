# Telecom Paristech
# IMA201 - 2017/2018
# Projet: detection d'anomalie RX (tuberculose)
#
# Prof: Isabelle Bloch
# 
# etudiants: Camille Ruppli et Renata Baptista
# Part 2/4
import numpy as np
import cv2

T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4_5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8_5ansNormale-distension","Rx11ansNormale-sdbronchique"]

for i in range(len(T)):
    img = cv2.imread('Lungsonly/lungsonly_'+T[i]+'.jpg')
    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 4
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    cv2.imwrite('Kmeans/kmeans4_'+T[i]+'.jpg',res2)