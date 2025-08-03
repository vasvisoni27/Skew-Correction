import cv2
import numpy as np
img=cv2.imread("c:/Users/VASVI SONI/Downloads/Digital-image-of-text-having-30-degree-of-skewed-angle (1).png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.bitwise_not(gray)
cv2.imshow('gray not',gray)
thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow('thresh',thresh)
coords=np.column_stack(np.where(thresh>0))
print('coord',coords)
angle=cv2.minAreaRect(coords)[-1]
if angle<-45:
    angle=-(90+angle)
else:
    angle=-angle
print(angle)
(h,w)=img.shape[:2]
centre=(w//2,h//2)
m=cv2.getRotationMatrix2D(centre,angle,1.0)
rotated=cv2.warpAffine(img,m,(w,h),borderMode=cv2.BORDER_REPLICATE)
cv2.imshow("input",img)
cv2.imshow("rotated",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
