import cv2
import numpy as np

I = cv2.imread('ExamPhoto/anh5.jpg')
cv2.imshow("Image I", I)

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(0.11 * I[i][j][0]) + int(0.5 * I[i][j][1]) + int(0.39 * I[i][j][2])
cv2.imshow("Image Ig", Ig)
print("Mức xám lớn nhất của ảnh Ig: ", np.max(Ig))

print("Mức xám lớn nhất của ảnh Ig: ", np.max(Ig))
print("Mức xám nhỏ nhất của ảnh Ig: ", np.min(Ig))
print("Mức xám trung bình của ảnh Ig: ", np.mean(Ig))

thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)

contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_cv = 0.0
contours_max = []
for i in contours:
    if cv2.arcLength(i, True) > max_cv/3.0:
        max_cv = cv2.arcLength(i, True)
        contours_max = i
print("Giá trị max_cv = ", max_cv)
cv2.drawContours(I, [contours_max], -1, (0, 255, 255), 3)
cv2.imshow("picture after drawing", I)
cv2.waitKey(0)
