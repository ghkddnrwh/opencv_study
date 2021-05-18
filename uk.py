import cv2
import numpy as np
import sys

video = cv2.VideoCapture('move.mp4')

if not video.isOpened():
    print('video open failed')
    sys.exit()

bs = cv2.createBackgroundSubtractorMOG2()

w = video.get(cv2.CAP_PROP_FRAME_WIDTH)
h = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = round(video.get(cv2.CAP_PROP_FPS))
delay = round(1000 / fps)

print(w, h)
print(fps)
print(delay)

while True:
    ret, frame = video.read()

    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame_mask = bs.apply(gray_frame)
    frame_back = bs.getBackgroundImage()

    count, _, stats, _ = cv2.connectedComponentsWithStats(frame_mask)

    for i in range(1, count):
        x, y, w, h, area = stats[i]

        if(area < 500):
            continue

        cv2.rectangle(frame, (x, y, w, h), (255, 0, 0), 1)

    cv2.imshow('frame', frame)
    cv2.imshow('back', frame_back)
    cv2.imshow('frame_mask', frame_mask)    

    if cv2.waitKey(10) == 27:
        break

video.realease()
cv2.destroyAllWindows()