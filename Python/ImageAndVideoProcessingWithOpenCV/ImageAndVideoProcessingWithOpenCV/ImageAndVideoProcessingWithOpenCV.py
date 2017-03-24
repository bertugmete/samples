import cv2
#blue,red,green icin : '0' ; black-white : '1' , transparance : -1
#numpy array olarak tutuyor.
#RESIZE, SHOW, WRITE IMAGE  
img = cv2.imread("galaxy.jpg",0)

#print(img.ndim)

resized_image = cv2.resize(img,(int(img.shape[1] / 2),int(img.shape[0] / 2)))

cv2.imwrite("Galaxy_resized.jpg",resized_image)
cv2.imshow("Galaxy",resized_image)

cv2.waitKey(5000)

cv2.destroyAllWindows()