import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread('ExamPhoto/hat1.PNG')
cv2.imshow("Channel B of image I", I[:, :, 0])

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("Channel H of image Ihsv", Ihsv[:, :, 0])
print("Giá trị mức xám trung bình của kênh S ", np.mean(Ihsv[:, :, 1]))

HistogramS = cv2.calcHist([Ihsv[:, :, 1]], [0], None, [256], [0, 256])
plt.plot(HistogramS)
plt.show()

Is = cv2.blur(Ihsv[:, :, 2], (3, 3))
y = 9
x = 11
print("Các mức xám trong lận cận 5x5 điểm ảnh")
for i in range(-2, 3):
    for j in range(-2, 3):
        if y + i >= 0 & y + i <= I.shape[0] - 1 & x + j >= 0 & x + j <= I.shape[1] - 1:
            print(Ihsv[:, :, 2][y + i][x + j])
thresh, Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_OTSU)
Contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_cv = 0
cnt_max = []
for i in Contours:
    if cv2.arcLength(i, True) > max_cv:
        max_cv = cv2.arcLength(i, True)
        cnt_max = i
cv2.drawContours(I, [cnt_max], -1, (0, 255, 255), 3)
cv2.imshow("image I", I)
cv2.waitKey(0)
