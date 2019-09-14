"""
Use my name as the screen locator!!!
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

tile = cv2.imread('resources/kss39.png', -1)
table = cv2.imread('resources/table.png', -1)

# Initiate STAR detector
orb = cv2.ORB_create(nfeatures=7000, fastThreshold=3, edgeThreshold=3)

# find the keypoints with ORB
kp_tile, des_tile = orb.detectAndCompute(tile, None)
kp_table, des_table = orb.detectAndCompute(table, None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

# Match descriptors.
matches = bf.match(des_tile, des_table)

# Sort them in the order of their distance.
matches = sorted(matches, key=lambda x: x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(tile, kp_tile, table, kp_table, matches[:70], None, flags=2)

cv2.imwrite('output/name_tag_locator.png', img3)

# Need to draw only good matches, so create a mask
matchesMask = [[0, 0] for i in range(len(matches))]

# ratio test as per Lowe's paper
for i, (m, n) in enumerate(matches):
    if m.distance < 0.7 * n.distance:
        matchesMask[i] = [1, 0]

draw_params = dict(matchColor=(0, 255, 0),
                   singlePointColor=(255, 0, 0),
                   matchesMask=matchesMask,
                   flags=0)

img3 = cv2.drawMatchesKnn(tile, kp_tile, table, kp_table, matches, None, **draw_params)

plt.imshow(img3), plt.show()
