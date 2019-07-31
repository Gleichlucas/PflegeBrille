import cv2
import numpy as np
import os

cap = cv2.VideoCapture('testbilder.mp4')

try:
    if not os.path.exists('data_s2'):
        os.makedirs('data_s2')
except OSError:
    print ('Error: Creating directory of data_s')

currentFrame = 0
while(True):
    i = 0
    while (i < 5):
        ret, frame = cap.read()
        i = i + 1
    name = './data_s2/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    currentFrame += 1

cap.release()
cv2.destroyAllWindows()
