#오재표 22012191 
import numpy as np
import cv2

imgfile='window.jpg'

img=cv2.imread(imgfile, cv2.IMREAD_COLOR)
cv2.imshow('img', img) 
height, width, channel = img.shape
b = img[..., 0]
g = img[..., 1]
r = img[..., 2]

y = np.zeros((height, width), dtype=np.double)
cb = np.zeros((height, width), dtype=np.double)
cr = np.zeros((height, width), dtype=np.double)

ycbcr1=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
rgb1=cv2.cvtColor(ycbcr1, cv2.COLOR_YCR_CB2BGR)

for i in range(height):
    for j in range(width):
        y[i][j] = 0.299 * r[i][j] + 0.587 * g[i][j] + 0.114 * b[i][j] 
        cr[i][j] = 0.511 * r[i][j] - 0.428 * g[i][j] - 0.083 * b[i][j] + 128
        cb[i][j] = - 0.172 * r[i][j] - 0.339 * g[i][j] + 0.511 * b[i][j] + 128
        
ycbcr2=(np.dstack((y,cr,cb))).astype(np.uint8)

for i in range(height):
    for j in range(width):
        b[i][j] = y[i][j]  + 1.372 * ( cb[i][j] - 128 )
        g[i][j] = y[i][j] - 0.698 * (cr[i][j] - 128) - 0.336 * ( cb[i][j] - 128)
        r[i][j] = y[i][j] + 1.371 * (cr[i][j] - 128)
        
rgb2=(np.dstack((b,g,r))).astype(np.uint8)


cv2.imshow('ycbcr1', ycbcr1)
cv2.imshow('rgb1', rgb1)
cv2.imshow('ycbcr2', ycbcr2)
cv2.imshow('rgb2', rgb2)
cv2.waitKey(0)