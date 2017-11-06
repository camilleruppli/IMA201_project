import cv2
import numpy as np
from matplotlib import pyplot as plt

#root = "/Users/camilleruppli/Desktop/Telecom/IMA/IMA201/"
T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4_5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8_5ansNormale-distension","Rx11ansNormale-sdbronchique"]


for i in range(len(T)):
    img = cv2.imread(T[i]+'.jpg')
    color = ('b','g','r')
    for j,col in enumerate(color):
        histr = cv2.calcHist([img],[j],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
        #plt.show() doen't work on my computer anymore
        plt.savefig('Histograms/histo_'+T[i]+'.png')
        plt.close()



