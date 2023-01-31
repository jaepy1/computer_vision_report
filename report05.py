import numpy as np
import cv2

imgfile='window.jpg'
img=cv2.imread(imgfile,cv2.IMREAD_COLOR)

ycbcr=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
y,cr,cb=cv2.split(ycbcr)

y1=cv2.equalizeHIst(y)
ycbcr1=(np.dstack((y1,cr,cb))).astype(np.uint8)
rgb1=cv2.cvtColor(ycbcr1,cv2.COLOR_YCR_CB2BGR)

function_psnr=cv2.PSNR(img,rgb1)
print("PSNR implemented by function:" ,function_psnr)

