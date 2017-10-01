import cv2
import matplotlib.pyplot as plt
import numpy as np
#root = "/Users/camilleruppli/Desktop/Telecom/IMA/IMA201/"

im=cv2.imread("result_testblack.jpg",0)
rows=im.shape[1]
columns=im.shape[0]
numbers=np.linspace(0,rows-1,rows)
S=[]
for j in range(0,rows):
    T=[]
    for i in range(columns):
        T.append(im[i,j])
    S.append(sum(T))
plt.plot(numbers,S)
plt.savefig("testsum.png")

k=0
for i in range(len(S)):
    if(S[i]!=0):
        k=i
print(k+1)
print(S[k])
im1=im.copy()

cv2.rectangle(im1, (k,1), (1899, 1819), (0, 255, 0), 2)
cv2.imwrite('lungsonly.jpg', im1)







