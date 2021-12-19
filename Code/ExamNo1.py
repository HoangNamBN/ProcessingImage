import cv2
import numpy as np

I = cv2.imread('ExamPhoto/the_cancuoc_congdan.jpg')
cv2.imshow("Channel B of photo I", I[:, :, 0])

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(0.11 * I[i][j][0]) + int(0.5 * I[i][j][1]) + int(0.39 * I[i][j][2])
cv2.imshow("Image Ig", Ig)

thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)

Im = cv2.blur(Ig, (5, 5))

contours, _ = cv2.findContours(Im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (255, 0, 0), 3)
cv2.imshow("picture after drawing", I)

cv2.waitKey(0)
