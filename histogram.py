# coding=utf-8
from __future__ import print_function
from PIL import Image
import matplotlib.pyplot as plt
root = "/Users/camilleruppli/Desktop/Telecom/IMA/IMA201/"

T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4,5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8,5ansNormale-distension","Rx11ansNormale-sdbronchique"]

for i in range(len(T)):
    try:
        im = Image.open(root+T[i]+".jpg")
        histo = im.histogram()
        plt.plot(histo)
        plt.savefig(root+"histogramme"+T[i])
        plt.close()
    except IOError:
        print("could not open image")

        #bla bla test
        #bla bla test 2






