import cv2
import numpy as np

I = cv2.imread('ExamPhoto/anh5.jpg')
cv2.imshow("I", I)
print("Tỉ lệ giữa giá trị độ cao và độ rộng của ảnh I là: ", I.shape[0]/I.shape[1])

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("Channel H of photo Ihsv", Ihsv[:,:,0])
print("Mức xám trung bình của ảnh Ig: ", np.mean(Ihsv[:,:,1]))

Is = cv2.medianBlur(Ihsv[:,:,1], 5)
cv2.imshow("Is", Is)

thresh, Ib = cv2.threshold(255-Is, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("Ib", Ib)
contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_cv = 0.0
contours_max = []
for i in contours:
    if cv2.arcLength(i, True) > max_cv:
        max_cv = cv2.arcLength(i, True)
        contours_max = i
cv2.drawContours(I, [contours_max], -1, (0, 255, 255), 3)
cv2.imshow("picture after drawing", I)

def GrayLevelStretch(Ig):
    min = np.min(Ig)
    max = np.max(Ig)
    aLUT = np.zeros(256, dtype='uint8')
    for i in range(0, 256):
        aLUT[i] = (255 * (i - min))//(max - min)
    for j in range(Ig.shape[0]):
        for k in range(Ig.shape[1]):
            Ig[i][j] = aLUT[Ig[i][j]]
    return Ig

Iv2= GrayLevelStretch(Ihsv[:,:,2])
cv2.imshow('gian muc xam kenh V',Iv2)

I = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("I new", I)
cv2.waitKey(0)