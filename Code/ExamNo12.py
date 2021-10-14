import cv2

I = cv2.imread('ExamPhoto/I04.jpg')
print("Tỉ lệ giữa giá trị độ cao và độ rộng của ảnh I là: ", I.shape[0] / I.shape[1])

I2 = cv2.resize(I, (256, 256))
cv2.imshow("Image I2", I2)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("Channel S of photo Ihsv", Ihsv[:, :, 1])

Ihsv[:, :, 1] = cv2.medianBlur(Ihsv[:, :, 1], 3)
I3 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("Image I3", I3)

Ihsv[:, :, 1] = cv2.equalizeHist(Ihsv[:, :, 1])
cv2.imshow("HistogramS", Ihsv[:, :, 1])

I4 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("Image I4", I4)

cv2.waitKey(0)
