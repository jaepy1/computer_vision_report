import numpy as np
import cv2

imgfile = 'image2.jpg'
img=cv2.imread(imgfile, cv2.IMREAD_COLOR)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()