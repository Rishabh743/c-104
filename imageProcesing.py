import cv2
img=cv2.imread("butterfly.jpg")
#cv2.imshow("images",img)
#cv2.waitKey(0)
greyimg=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("greyimg",greyimg)
cv2.waitKey(0)