import cv2
import numpy
import sys

video = cv2.VideoCapture('move2.mp4')

w, h = 1500, 730

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D','I','V','X'
out = cv2.VideoWriter('move.mp4', fourcc, 30, (w, h))

while True:
    ret, full_frame = video.read()

    if not ret:
        break

    frame = full_frame[350:, :1500]
    out.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

video.realease()
cv2.destroyAllWindows()