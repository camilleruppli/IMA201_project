import cv2
import matplotlib.pyplot as plt
import numpy as np

#root = "/Users/camilleruppli/Desktop/Telecom/IMA/IMA201/"

T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4_5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8_5ansNormale-distension","Rx11ansNormale-sdbronchique"]

for k in range(len(T)):
    im=cv2.imread(T[k]+'.jpg',0)
    ret, thresh = cv2.threshold(im, 127, 255, 0)
    imgray,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Find the index of the largest contour
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt=contours[max_index]
    im1=im.copy()
    x,y,w,h = cv2.boundingRect(cnt)

    contRect=np.array([[x,y],[x,y+h],[x+w,y+h],[x+w,y]])
    stencil=np.zeros(im.shape).astype(im.dtype)
    color=[255,255,255]
    cv2.fillPoly(stencil,[contRect],color)
    result=cv2.bitwise_and(im1,stencil)

    cv2.imwrite("boundingBox/blackBox_"+T[k]+".jpg",result)

    im=cv2.imread("boundingBox/blackBox_"+T[k]+".jpg",0)
    im2=cv2.imread("imagesBlack/result_testblack_"+T[k]+".jpg",0)
    rows=im2.shape[1]
    columns=im2.shape[0]
    numbers=np.linspace(0,columns-1,columns)
    S=[]
    for j in range(0,columns):
        V=[]
        for i in range(rows):
            V.append(im2[j,i])
        S.append(sum(V))
    plt.plot(numbers,S)
    plt.savefig("Sum/testsum_"+T[k]+".png")
    plt.close()
    threshold=0
    m=np.median(np.array(S))
    print("Median for image ",T[k],"=",m)
    for i in range(len(S)):
        if(S[i]>m): #100
            threshold=i
    im1=im.copy()

    for l in range(threshold,rows):
        im1[l:]=0

    #cv2.rectangle(im1, (0,threshold), (1900, 1820), (255, 0, 0), 2)
    cv2.imwrite('Lungsonly/lungsonly_'+T[k]+'.jpg', im1)







