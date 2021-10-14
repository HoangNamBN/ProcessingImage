import cv2
import matplotlib.pyplot as plt

I = cv2.imread('ExamPhoto/I04.jpg')
print("Tỉ lệ giữa giá trị độ cao và độ rộng của ảnh I là: ", I.shape[0]/I.shape[1])

I2 = cv2.resize(I, (256, 256))
cv2.imshow("Image I2", I2)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("Channel S of photo Ihsv", Ihsv[:,:,1])

Ivb = cv2.Canny(Ihsv[:,:,2], 0, 255)

HistogramS = cv2.calcHist([Ihsv[:,:,1]], [0], None, [256], [0, 256])
plt.plot(HistogramS)
plt.title("Histogram of Channel S")
plt.show()

cv2.waitKey(0)