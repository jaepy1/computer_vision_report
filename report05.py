#오재표 22012191
import numpy as np
import cv2

imgfile='window.jpg'
img=cv2.imread(imgfile,cv2.IMREAD_COLOR)

ycbcr=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
y,cr,cb=cv2.split(ycbcr)

# 1번 opencv 함수를 사용한다.
y1=cv2.equalizeHist(y) #y정보 만으로 Histogram Equalization
ycbcr1=(np.dstack((y1,cr,cb))).astype(np.uint8) #merge
rgb1=cv2.cvtColor(ycbcr1,cv2.COLOR_YCR_CB2BGR) # 복원

function_psnr=cv2.PSNR(img,rgb1)
print("PSNR implemented by function:" ,function_psnr)

#2번 Histogram Equalization 수식 이용
height, width, channel = img.shape
total_pixel=height*width #전체 픽셀 수

hist,bins = np.histogram(y.flatten(),256,[0,256])# y정보 Histogram
sum=hist.cumsum()

hist_equal=np.uint8(np.ceil((255+1)/(total_pixel)*sum)-1) 
#Histogram Equalization

y2=hist_equal[y] #y
ycbcr2=(np.dstack((y2,cr,cb))).astype(np.uint8) #merge
rgb2=cv2.cvtColor(ycbcr2,cv2.COLOR_YCR_CB2BGR) #복원

formula_psnr=cv2.PSNR(img,rgb2)
print("PSNR implemented by formula:" ,formula_psnr)

cv2.imshow('img',img)
cv2.imshow('rgb_function',rgb1)
cv2.imshow('rgb_formula',rgb2)
cv2.waitKey(0)