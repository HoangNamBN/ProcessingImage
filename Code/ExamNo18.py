import cv2
import numpy as np

I = cv2.imread("ExamPhoto/anh5.jpg")
cv2.imshow("Image I", I)

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(I[i][j][2] * 0.39) + int(I[i][j][1] * 0.5) + int(I[i][j][0] * 0.11)
cv2.imshow("Image Ig", Ig)
print("Mức xám trung bình của ảnh Ig", np.mean(Ig))

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
print("Mức xám lớn nhất của kênh S của ảnh Ihsv", np.max(Ihsv[:, :, 1]))

Thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("Image Ib", Ib)

Contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_cv = 0.0
cnt_max = []
for i in Contours:
    if cv2.arcLength(i, True) > max_cv / 3.0:
        max_cv = cv2.arcLength(i, True)
        cnt_max = i
cv2.drawContours(I, [cnt_max], -1, (0, 255, 255), 3)
cv2.imshow("Image I1", I)
cv2.waitKey(0)
