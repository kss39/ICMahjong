"""
This contour experiment can find proper tiles
in a small cropped image.
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt


rgb = cv2.imread('resources/small_table.png', -1)
orig = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(orig, 200, 255, cv2.THRESH_BINARY)

cv2.imwrite('output/thresh_smallhand.png', thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

ref = contours[0]
ref_area = cv2.contourArea(ref)

result = []
for cnt in contours:
    ratio = cv2.contourArea(cnt) / ref_area
    if 0.97 < ratio < 1.03:
        result.append(cnt)

img = cv2.drawContours(rgb, result, -1, (0, 0, 255, 255), 3)

cv2.imwrite('output/contour_smallhand.png', img)
