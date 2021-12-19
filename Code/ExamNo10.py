import cv2
import numpy as np

I = cv2.imread('ExamPhoto/anh5.jpg')
cv2.imshow("Image I", I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("Channel S of Ihsv", Ihsv[:,:,1])
print("Mức sáng lớn nhất kênh V của ảnh Ihsv: ", np.max(Ihsv[:,:,2]))

Iv = cv2.blur(Ihsv[:,:,2], (3,3))
cv2.imshow("Image Iv", Iv)

thresh, Ib = cv2.threshold(Iv, 0, 255, cv2.THRESH_OTSU)

contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_cv = 0.0
contours_max = []
for i in contours:
    if cv2.arcLength(i, True) > max_cv/3.0:
        max_cv = cv2.arcLength(i, True)
        contours_max = i
cv2.drawContours(I, [contours_max], -1, (0, 255, 255), 3)
cv2.imshow("picture after drawing", I)

HistorgramV = cv2.equalizeHist(Ihsv[:,:,2])
cv2.imshow("HistorgramV",HistorgramV)

I = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("I new", I)

cv2.waitKey(0)