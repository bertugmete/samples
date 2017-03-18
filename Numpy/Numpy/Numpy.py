import numpy
#numpy ile image'in renk kodlarini gosterir. 
#0-26 arasi sayilar  uretir.
n = numpy.arange(27)
# 3x9'luk matris seklinde olusturur.
#n = n.reshape(3,9)

#3'luk 3x3'luk matris olusturur.
#n = n.reshape(3,3,3)
#print(n)

#m = numpy.asarray([123,12,123,12,33],[],[])

import cv2
#0 means gray
im_g = cv2.imread("C:\\Users\\Bertug\\Desktop\\smallgray.png",1)

#print(im_g)
#yeni bir image olusturmak icin
#cv2.imwrite("newsmall.png",im_g)

#print(im_g[0:2,2:4])

#im_g.T transpozunu alir.
#flat ile tek sutunda toplariz
#for i in im_g.flat:
#    print(i)
#horizontal stack
#ims = numpy.hstack((im_g,im_g))
#print(ims)

#vertical stack
ims = numpy.vstack((im_g,im_g))


lst = numpy.hsplit(ims,5)

lst = numpy.vsplit(ims,3)

print(lst)