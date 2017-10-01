import cv2
import numpy as np

#T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4,5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8,5ansNormale-distension","Rx11ansNormale-sdbronchique"]

#for i in range(len(T)):
im=cv2.imread('Rx1anNormale.jpg')
rows = im.shape[0]
columns = im.shape[1]
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
imgray,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Find the index of the largest contour
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]
im1=im.copy()
x,y,w,h = cv2.boundingRect(cnt)

for i in range(rows):
    for j in range(columns):
        pixel = im[i,j]
        if i<y or i>y+h:
            im1[i,j]=0
        if j<x or j>x+w:
            im1[i,j]=0
cv2.imwrite('testblack.png',im1)

im = cv2.imread('testblack.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
imgray, contours1, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
im1 = im.copy()
im2=im.copy()
cv2.drawContours(im1, contours1, -1, (255, 0, 0), 3)
partReal = 0
contoursBigger = []
for c in contours1:
    perimeter = cv2.arcLength(c,True)
    #print perimeter
    if perimeter > 100: #taille du contour
        contoursBigger.append(c)

cv2.drawContours(im2, contoursBigger, -1, (0,0,0), -1)
cv2.imwrite("result_testblack.jpg", im2)
print "Cleaning contours",len(contoursBigger)
cv2.imwrite("t_contours_testblack.png",im1)



