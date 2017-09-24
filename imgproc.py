import numpy as np
import cv2
img = cv2.imread("image.JPG")
cols = img.shape[1]
rows = img.shape[0]
center = (rows/2,cols/2)
angle =-90
pic = cv2.getRotationMatrix2D(center,angle,1)
shifted = cv2.warpAffine(img,pic,(cols,rows))
cv2.imshow('shifted',shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
