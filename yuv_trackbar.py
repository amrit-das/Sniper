import cv2
import numpy as np

def nothing(x):
	pass

# Create a black image, a window
img = np.zeros((300,300,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('Y','image',0,255,nothing)
cv2.createTrackbar('U','image',0,255,nothing)
cv2.createTrackbar('V','image',0,255,nothing)
cap = cv2.VideoCapture(2)
boln = True
while boln:
    y = cv2.getTrackbarPos('Y','image')
    u = cv2.getTrackbarPos('U','image')
    v = cv2.getTrackbarPos('V','image')

    img[:] = [y,u,v]
    img= cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    #cv2.imshow('image',img)
    boln,f = cap.read()
    img_yuv = cv2.cvtColor(f, cv2.COLOR_BGR2YUV)
    #cv2.imshow("g1",img_yuv)
    #img_yuv[:,:,2] = cv2.equalizeHist(img_yuv[:,:,2])
    #cv2.imshow("g2",img_yuv
    mask = cv2.inRange(img_yuv, (np.array([0,u-30,v-30])), (np.array([255,u+30,v+30])))
    cv2.imshow("Masking",mask)
    erode = cv2.erode(mask,None,iterations = 1)
    dilate = cv2.dilate(erode,None,iterations = 1)
    image,contours,hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
    #if len(contours)>0:
        #c = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(f,(x,y),(x+w,y+h),[255,0,0],2)
        #print x, y, w, h

    #img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    #cv2.imshow('Histogram equalized', f)
    if cv2.waitKey(25)&0xff==27:
	break

cap.release()
cv2.destroyAllWindows()
