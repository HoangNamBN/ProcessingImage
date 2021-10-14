import cv2
import numpy as np

I = cv2.imread('ExamPhoto/clother1.jpg')
cv2.imshow("Channel B of image I", I[:,:,0])

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("Channel S of inage Ihsv", Ihsv[:, :, 1])

print("Các độ xám lân cận 3x3 của pixel có toạ độ y = 10, x = 12 là: \n")
y = 10
x = 12
for i in range(-2, 3):
    for j in range(-2, 3):
        if(y + i >= 0 & y + i <= I.shape[0] - 1 & x + j >= 0 & x + j <= I.shape[1] -1):
            print(Ihsv[:, :, 1][y + i][x + j])

Im = cv2.blur(Ihsv[:, :, 2], (5, 5))
cv2.imshow("Image Im", Im)

contours, _ = cv2.findContours(Im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255),3)
cv2.imshow("Anh sau khi ve", I)
cv2.waitKey(0)