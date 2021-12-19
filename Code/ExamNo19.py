import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread("ExamPhoto/apple.jpg")
cv2.imshow("Channel R", I[:,:,2])

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(I[i][j][2] * 0.39) + int(I[i][j][1] * 0.5) + int(I[i][j][0] * 0.11)
cv2.imshow("Image Ig", Ig)
print("Mức xám trung bình của ảnh Ig", np.mean(Ig))

GradientX = cv2.Sobel(Ig, cv2.CV_64F, 1, 0, 3)
plt.imshow(GradientX, cmap='gray')
plt.title("GradientX")
plt.show()

Ie = cv2.Canny(Ig, 0, 255)
if Ie[100][120] == 255:
    print("Là điểm biên")
else:
    print("Không là điểm biên")

Thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_area = 0
cnt_max = []
for i in contours:
    if cv2.contourArea(i) > max_area:
        max_area = cv2.contourArea(i)
        cnt_max = i
cv2.drawContours(I, [cnt_max], -1, (0, 255, 255), 3)
cv2.imshow("Image i1", I)
cv2.waitKey(0)