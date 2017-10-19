import matplotlib as mpl
mpl.use('Agg')
import cv2
import numpy as np
import math
from skimage import data
from skimage.util import img_as_ubyte
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage import measure


T=["Rx1anNormale","Rx3ansFoyerInfGauche","Rx3ansNormaleFace","Rx3ansNormaleProfil","Rx4_5ansPneumopathieNecrosanteDroite","Rx4ansNormale","Rx8_5ansNormale-distension","Rx11ansNormale-sdbronchique"]
SIZE_GRID = (128,128)

for i in range(len(T)):
    im=cv2.imread('Lungsonly/lungsonly_'+T[i]+'.jpg', 0)

    rows=im.shape[0]
    columns=im.shape[1]
    print rows,columns

    colTotal = int(math.floor(columns/SIZE_GRID[0]))
    rowsTotal = int(math.floor(rows/SIZE_GRID[1]))
    print colTotal, rowsTotal
    allHisto = np.zeros((rowsTotal,colTotal))
    for col_index in range (colTotal):
        for row_index in range (rowsTotal):
            histo = []
            aux = list(range(SIZE_GRID[0]))
            aux = np.array(aux)
            piece = im[aux*(row_index+1),:][:,aux*(col_index+1)]
            print "Comparacao"
            print im[158,:], im[158][:]
            print im[159,:], im[159][:]
            print piece
            #if (np.all(piece, np.zeros(SIZE_GRID))!=0):
            #print "ei"
            histo = np.histogram(piece)
            #cv2.imwrite("histo/histo_"+"col"+str(col_index)+"_"+"row"+str(row_index)+"_"+T[i]+".jpg",histo)
            #allHisto[row_index,col_index] = histo
            mpl.pyplot.hist(histo, bins='auto')
            mpl.pyplot.savefig("histo/histo_"+T[i]+"col_index"+str(col_index)+"_"+"row_index"+str(row_index)+".jpg")
