import cv2
import numpy as np

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

I = cv2.imread('ExamPhoto/anh5.jpg')
cv2.imshow("Image I", I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("Channel H of image Ihsv", Ihsv[:,:,0])
print("Giá trị mức sáng lớn nhất của kênh S của ảnh Ihsv", np.max(Ihsv[:,:,1]))

Is = cv2.blur(Ihsv[:,:, 1], (7,7))
cv2.imshow("Is", Is)

thresh, Ib = cv2.threshold(255- Is, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max = 0.0
contour_max = []
for i in contours:
    if cv2.arcLength(i, True) > max:
        max = cv2.arcLength(i, True)
        contour_max = i
cv2.drawContours(I, [contour_max], -1, (0,0,255), 3)
cv2.imshow("picture after drawing", I)

Iv2= GrayLevelStretch(Ihsv[:,:,2])
cv2.imshow('gian muc xam kenh V',Iv2)

I = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("I new", I)
cv2.waitKey(0)