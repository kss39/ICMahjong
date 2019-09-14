import cv2

img = cv2.imread('resources/hand.png', 0)


ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
cv2.imwrite('output/thresh_binary.png', thresh1)
cv2.imwrite('output/thresh_tozero.png', thresh2)

# TOZERO is better