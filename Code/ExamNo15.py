import cv2
import numpy as np

I = cv2.imread('ExamPhoto/Coins.jpg')
cv2.imshow("Image I", I)
print("Height of I", I.shape[0])
print("Width of I", I.shape[1])

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(0.11 * I[i][j][0]) + int(0.5 * I[i][j][1]) + int(0.39 * I[i][j][2])
cv2.imshow("Image Ig", Ig)
print("Mức xám trung bình của ảnh Ig: ", np.mean(Ig))

print("Các độ xám lân cận 3x3 của pixel có toạ độ y = 109, x = 130 là: \n")
y = 109
x = 130
for i in range(-2, 3):
    for j in range(-2, 3):
        if(y + i >= 0 & y + i <= I.shape[0] - 1 & x + j >= 0 & x + j <= I.shape[1] -1):
            print(Ig[y + i][x + j])

Ie = cv2.Canny(Ig, 0, 255)
if Ie[109][130] == 255:
    print("là điểm biên của ảnh Ig theo phép dò biên Canny")
else:
    print("không là điểm biên của ảnh Ig theo phép dò biên Canny")

thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255),3)
cv2.imshow("Anh sau khi ve", I)
cv2.waitKey(0)