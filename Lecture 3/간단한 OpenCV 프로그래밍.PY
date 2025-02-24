import numpy as np
import cv2
image = np.zeros((300, 400), np.uint8)
image.fill(200)

cv2.imshow("window title", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

## 300행 , 400크기의 행렬 생성하여 행렬의 모든 원소의 값을 회색 (200)으로 지정
##이 행렬을 "window title" 이름의 윈도우에 영상으로 표시