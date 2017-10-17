import cv2
import numpy as np
y,u,v = 0,142,56
def sniper():
    cap = cv2.VideoCapture(1)
    rec=True
    while rec:
    	rec,img = cap.read()
    	img_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
    	
    	blur = cv2.GaussianBlur(img_yuv,(11,11),2)
    	ball = cv2.inRange(blur, (np.array([0,u-30,v-30])), (np.array([255,u+30,v+30])))

    	im_floodfill = ball.copy()
        h, w = ball.shape[:2]\

        mask = np.zeros((h+2, w+2), np.uint8)
        cv2.floodFill(im_floodfill, mask, (0,0), 255)

        fill = cv2.bitwise_and(im_floodfill,im_floodfill,mask = ball)

        if cv2.waitKey(25)&0xff==27:
            break

        cv2.rectangle(img, (290,210), (350,270), (255,255,255),2)
        crop_img = fill[210:270, 290:350]

        images,s_contour,hierarchy = cv2.findContours(crop_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        images,contour,hierarchy = cv2.findContours(fill,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(img, contour, -1, (0,255,0), 2)

        cv2.imshow("",img)

        if len(contour)>=1:
        	cnt = contours[0]
        	(x,y),radius = cv2.minEnclosingCircle(cnt)
        	center = (int(x),int(y))
        	point = cv2.circle(img,center,radius,(0,0,255),2)
        	print center
        if len(s_contour)>=1:
			print "Found"
			break

	cv2.destroyAllWindows()
    cap.release()

sniper()


