import cv2
import numpy as np

I = cv2.imread("ExamPhoto/watch.jpg")
cv2.imshow("Channel B of Image I", I[:, :, 0])

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("channel s of Image Ihsv", Ihsv[:, :, 1])
print("Mức xám trung bình của Channel V of Ihsv", np.mean(Ihsv[:, :, 2]))

Is = cv2.blur(Ihsv[:, :, 1], (5, 5))
cv2.imshow("Image Is", Is)

Thresh, Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_OTSU)
Contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_cv = 0
cnt_max = []
for i in Contours:
    if cv2.arcLength(i, True) > max_cv:
        max_cv = cv2.arcLength(i, True)
        cnt_max = i
cv2.drawContours(I, [cnt_max], -1, (0, 255, 255), 3)
cv2.imshow("Image I1", I)


def Giantuytinh(Ik):
    max = np.max(Ik)
    min = np.min(Ik)
    Ic = np.zeros(256, dtype='uint8')
    for i in range(0, 256):
        Ic[i] = (256 * (i - min)) // (max - min)
    for j in range(I.shape[0]):
        for k in range(I.shape[1]):
            Ik[j][k] = Ic[Ik[j][k]]
    return Ik

Iv = Giantuytinh(Ihsv[:, :, 2])
cv2.imshow("Iv", Iv)

I = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2RGB)
cv2.imshow("Image I sau khi biến đổi", I)
cv2.waitKey(0)