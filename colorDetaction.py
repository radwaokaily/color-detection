import cv2
import numpy as np

#TrackBar
def empty(x):
    pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",(400,250))
cv2.createTrackbar("Hue Min","TrackBars",3,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",128,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",5,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",28,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

#Read Image
img=cv2.imread('D:/ComputerVision_cv/34287_1__63596.jpg')
imgResized=cv2.resize(img,(400,400))
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
imgHSVResized=cv2.resize(imgHSV,(400,400))
while True:
    h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max=cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min=cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max=cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min=cv2.getTrackbarPos("Val Min","TrackBars")
    v_max=cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSVResized,lower,upper)
    imgResult=cv2.bitwise_and(imgResized,imgResized,mask=mask)
    #Show Image
    cv2.imshow("original",imgResized)
    cv2.imshow("hsv",imgHSVResized)
    cv2.imshow("mask",mask)
    cv2.imshow("result",imgResult)
    cv2.waitKey(1)