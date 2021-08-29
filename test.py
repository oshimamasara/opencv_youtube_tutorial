import cv2
import numpy as np
import utils

path = '2.jpg'
wP = 210
hP = 297
scale = 3


img = cv2.imread(path)

img, conts = utils.getContours(img, minArea=68000, filter=4)
if len(conts) != 0:
    print('確認')
    print(conts[0])
    biggest = conts[0][2]
    print('BIGGEST')
    print(biggest)
    imgWrap = utils.warpImg(img, biggest, wP, hP)
    cv2.imshow('A4', imgWrap)

img = cv2.resize(img, (0,0), None, 0.5, 0.5)
cv2.imshow('Original', img)
cv2.waitKey(12000)
cv2.destroyAllWindows()