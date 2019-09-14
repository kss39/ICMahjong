"""
Generates the train tile set pngs.
"""

import cv2
from matplotlib import pyplot as plt

hand = cv2.imread('resources/hand.png', 0)

# Threshold the image first
ret, thresh = cv2.threshold(hand, 127, 255, cv2.THRESH_TOZERO)

w, h = thresh.shape[::-1]
w_step, h_step = int(w / 10), int(h / 4)

for simple in range(4):
    start_x = 0
    start_y = int(h * simple / 4)
    for number in range(10):
        one_tile = thresh[start_y:start_y + h_step - 1, start_x:start_x + w_step - 1]
        cv2.imwrite('resources/tiles_torezo/' + str(simple * 10 + number) + '.png', one_tile)
        start_x += w_step
