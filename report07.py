#오재표 22012191
import numpy as np 
import cv2

cap=cv2.VideoCapture('video.mp4')

while True:
    ret, frame = cap.read() #무한 루프에서 이미지를 계속 불러온다. 
    frame = cv2.resize(frame,(600,500)) #크기조절
    
    if not ret: #입력 못받았을 경우 오류출력
        print('error')
        break

    cv2.imshow('video',frame)
    
    ycbcr=cv2.cvtColor(frame,cv2.COLOR_BGR2YCR_CB)
    y,cr,cb=cv2.split(ycbcr) #분할
    
    edges=cv2.Canny(y,50,150,apertureSize=3) #Canny Edge Detection진행
    cv2.imshow('Canny Edge Detection',edges)
    
    lines = cv2.HoughLines(edges,1,np.pi/180,150) #Hough Line Detection진행
    
    #원본 RGB에서 찾아진 Line 성분 겹쳐서 출력
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),1)
    
    cv2.imshow('Hough Line Detection',frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()