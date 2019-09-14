'''
This module is the experiment of template finding in OpenCV.
Can be used to restart round, click UI, etc.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

z7 = cv2.imread('resources/7zcrop.png', 0)
table = cv2.imread('resources/table.png', 0)
table_orig = cv2.imread('resources/table.png', -1)

w, h = z7.shape[::-1]

res = cv2.matchTemplate(table, z7, cv2.TM_SQDIFF_NORMED)
# loc = np.where(res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(table, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(table_orig, top_left, bottom_right, (0, 0, 255, 255), 10)

cv2.imwrite('output/result.png', table_orig)


