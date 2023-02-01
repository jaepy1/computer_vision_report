#report 03 오재표 
import numpy as np
import math
import cv2

def psnr(original, contrast):
    mse = np.mean((original - contrast) ** 2) #평균 제곱 오차
    if mse == 0:
        return 100#오차가 0 즉 같은 그림일 경우
    max=255
    return 20 * math.log10(max / math.sqrt(mse))#psnr

imgfile='window.jpg'

img=cv2.imread(imgfile, cv2.IMREAD_COLOR) # RGB원본
cv2.imshow('img', img) 

ycbcr=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
rgb=cv2.cvtColor(ycbcr, cv2.COLOR_YCR_CB2BGR)# 복원

opnecv_psnr=cv2.PSNR(img,rgb)#opencv 사용
formula_psnr=psnr(img,rgb)#수식을 사용

print("implemented by function : ",opnecv_psnr)
print("implemented by formula :  ",formula_psnr)