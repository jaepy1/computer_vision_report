#오재표 22012191
import numpy as np
import cv2

imgfile='window.jpg'
img=cv2.imread(imgfile,cv2.IMREAD_COLOR)

ycbcr=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
y,cr,cb=cv2.split(ycbcr) #분할

for i in range(5): #3x3 averaging filter를 연속 5번 한다.
    y=cv2.blur(y,(3,3)) 
    
ycbcr2=(np.dstack((y,cr,cb))).astype(np.uint8) #filtering 된 y를 merge
rgb=cv2.cvtColor(ycbcr2,cv2.COLOR_YCR_CB2BGR)#복원

psnr=cv2.PSNR(img,rgb) #psnr
print('PSNR : ',psnr)

cv2.imshow('img',img)
cv2.imshow('rgb',rgb)
cv2.waitKey(0)