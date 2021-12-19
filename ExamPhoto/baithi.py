import cv2
import numpy as np 

#Hien thi anh
I = cv2.imread("anh5.jpg")
cv2.imshow("Anh I",I)

#Chuyen anh sang bieu dien HSV . Hien thi kenh H
Ihsv = cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
(h,s,v) = cv2.split(Ihsv)
cv2.imshow("Kenh H",h)

#Xac dinh gia tri muc sang lon nhat cua kenh S cua anh Ihsv
max_muc_sang = np.max(s)
print(max_muc_sang) 

#Lam tron anh kenh S va Hien thi anh Is
Is = cv2.medianBlur(s,7)
cv2.imshow("Anh lam tron kenh S",Is)



cv2.waitKey()