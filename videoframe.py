import cv2
import numpy as np


path='TownCentreXVID.avi'

vidcap = cv2.VideoCapture(path)
success,image = vidcap.read()
count = 0
while success:
    success,image = vidcap.read()
    cv2.imwrite("test/frame%d.jpg" % count, image)     # save frame as JPEG file
    count += 1