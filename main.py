import numpy as np
import cv2 as cv
from PIL import Image

from util import get_limits

yellow = [0, 225, 225] # Yellow color in BGR colors

cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()

    # Convert BGR Color to RSV color
    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerLimits, upperLimits = get_limits(color=yellow)

    # Getting the mask of all the pixels that belongs to the color we want to detect
    mask = cv.inRange(hsvImage, lowerLimits, upperLimits)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()
    print(bbox)

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)


    cv.imshow('frame', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()