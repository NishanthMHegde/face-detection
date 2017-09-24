import cv2
import numpy as np

pic = np.zeros((500,500,3),dtype ='uint8')
cv2.rectangle(pic,(0,0),(500,200),(123,156,200),3,lineType=8,shift=0)
cv2.line(pic,(100,150),(400,150),(45,56,16),3)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic,'Udemy',(100,100),font,3,(145,145,156),4)
cv2.circle(pic,(250,300),40,(135,156,200),3)
cv2.imshow('dark',pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
