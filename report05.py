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

height, width,channel = img.shape
total_pixel=height*width
hist,bin=np.histogram(y.ravel(),256,[0.256])
sum=hist.cumsum()

hist_equal=np.uint8(np.ceil((255+1)/(total_pixel)*sum)-1)

y2=hist_equal[y]
ycbcr2=(np.dstack((y2,cr,cb))).astype(np.uint8)
rgb2=cv2.cvtColor(ycbcr2,cv2.COLOR_YCR_CB2BGR)

formula_psnr=cv2.PSNR(img,rgb2)
print("PSNR implemented by formula:" ,formula_psnr)