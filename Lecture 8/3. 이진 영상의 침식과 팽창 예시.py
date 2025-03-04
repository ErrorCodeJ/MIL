import numpy as np
import cv2

src = cv2.imread('circuit.bmp', cv2.imread_grayscale)

se = cv2.getStructuringElement(cv2.NORPH_RECT, (5, 3))
dst1 = cv2.erode(src, se)

dst2 = cv2.dilate(src, None)