import numpy as np
import cv2

src = cv2.imread('leanna.bmp', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.add(src, 100)

dst2 = src + 100
#dst2 = np.clip(src + 100., 0, 255).astype(no.uint8)