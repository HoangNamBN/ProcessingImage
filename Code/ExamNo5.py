import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread('ExamPhoto/anh5.jpg')
cv2.imshow("Image I", I)

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(0.11 * I[i][j][0]) + int(0.5 * I[i][j][1]) + int(0.39 * I[i][j][2])
cv2.imshow("Image Ig", Ig)
print("Mức xám lớn nhất của ảnh Ig: ", np.max(Ig))

GradientX = cv2.Sobel(Ig, cv2.CV_64F, 1, 0, 3)
plt.subplot(2,2,1), plt.title("GradientX")
plt.imshow(GradientX, cmap='gray')

GradientY = cv2.Sobel(Ig, cv2.CV_64F, 0, 1, 3)
plt.subplot(2,2,2), plt.title("GradientY")
plt.imshow(GradientY, cmap='gray')
plt.show()

Ie = cv2.Canny(Ig, 0, 255)
print("Các độ xám lân cận 3x3 của pixel có toạ độ y = 179, x = 123 là: \n")
y = 179
x = 123
for i in range(-1, 2):
    for j in range(-1, 2):
        if(y + i >= 0 & y + i <= I.shape[0] - 1 & x + j >= 0 & x + j <= I.shape[1] -1):
            print(Ig[y + i][x + j])

thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255),3)
cv2.imshow("Anh sau khi ve", I)
cv2.waitKey(0)