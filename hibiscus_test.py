import cv2
import numpy as np
import random as rd
import scipy.ndimage

im=cv2.imread('index_01.png',0)
im1=im.copy()
im2=im.copy()
gradf=np.gradient(im1)

rows = im.shape[1]
columns = im.shape[0]
sigma=0.1
for i in range(rows):
    for j in range(columns):
        dfx=gradf[0][j][i]
        dfy=gradf[1][j][i]
        V=np.array([dfx,dfy])
        tensor=np.tensordot(V,V,0)
        #print(tensor)
        kernel = 1 / (2 * np.pi * sigma ** 2) * np.array([[1, np.exp(-1 / (2 * sigma ** 2))], [np.exp(-1 / (2 * sigma ** 2)), 1]])
        T = np.real(np.fft.ifft( np.fft.fft(tensor)*np.fft.fft(kernel) )) #circular convolution
        vp=np.linalg.eig(np.matrix(T))
        v1=vp[0][0]
        v2=vp[0][1]
        print(v1,v2)
        if(v1==0 and v2==0):
            print('both eigen values equal zero')
        else:
            E=np.sqrt(v1+v2)
            A=abs((v1-v2))*1.0/(v1+v2)
            im1[j][i]=E
            im2[j][i]=A
cv2.imwrite('testEH.jpg',im1)
cv2.imwrite('testAH.jpg',im2)


