import numpy as np
import cv2 as cv

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    # Check for red hue, which can be around 0 or 180
    if hsvC[0][0][0] < 10 or hsvC[0][0][0] > 170:
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([170, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit
