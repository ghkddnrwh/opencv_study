import cv2
import numpy as np
import sys

image = cv2.imread('color.jpg')

for i in range(4):
    x, y, w, h = cv2.selectROI(image)

    image_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    target = image_ycrcb[y:y+h, x:x+w]

    chan = [1, 2]
    hist_size = [128, 128]
    ranges = [0, 256, 0, 256]

    hist = cv2.calcHist([target], chan, None, hist_size, ranges)
    hist_norm = cv2.normalize(cv2.log(hist+1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    back = cv2.calcBackProject([image_ycrcb], chan, hist, ranges, 1)
    result = cv2.copyTo(image, back)

    cv2.imshow('back',result)
    cv2.waitKey()
    cv2.destroyAllWindows()


cv2.destroyAllWindows()