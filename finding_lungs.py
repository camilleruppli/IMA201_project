#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Télécom Paristech
# IMA201a - 2017
# Orientadora: Isabelle Bloch

# Authors: Camille Rippli - camille.ruppli@telecom-paristech.fr
#          Renata Baptista - baptista@telecom-paristech.fr



 #Libraries
# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image file")
#args = vars(ap.parse_args())

 # load the image
#image = cv2.imread(args["image"])
image = cv2.imread("Rx1anNormale.jpg")
print image.shape
lower = np.array([40, 40, 40])
upper = np.array([75, 75, 75])
shapeMask = cv2.inRange(image, lower, upper)

# find the contours in the mask
_ ,cnts , _ = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
print "I found %d black shapes" % (len(cnts))
#cv2.imshow("Mask", shapeMask)
for c in cnts:
	# draw the contour and show it
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.imwrite("Image.png", image)
	#cv2.imshow("Image", image)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
