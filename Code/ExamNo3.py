import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread('ExamPhoto/hat1.PNG')

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("Channel H of image Ihsv", Ihsv[:,:,0])
print("Giá trị mức sáng lớn nhất của kênh S của ảnh Ihsv", np.max(Ihsv[:,:,1]))

HistogramV = cv2.calcHist([Ihsv[:, :, 2]], [0], None, [256], [0, 256])
plt.plot(HistogramV)
plt.title("HistogramV")
plt.show()

Is = cv2.medianBlur(Ihsv[:,:,1], 5)
cv2.imshow("Is", Is)

thresh, Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max = 0.0
contour_max = []
for i in contours:
    if cv2.arcLength(i, True) > max:
        max = cv2.arcLength(i, True)
        contour_max = i
cv2.drawContours(I, [contour_max], -1, (0,0,255), 3)
cv2.imshow("picture after drawing", I)

cv2.waitKey(0)