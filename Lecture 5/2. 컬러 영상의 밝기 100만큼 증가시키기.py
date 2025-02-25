import numpy as np
import cv2

src = cv2.imread('lenna.bmp')

dst1 = cv2.add(src, (100, 100, 100, 0 ))

dst = np.clip(src + 100., 0, 255).astype(np.uint8)