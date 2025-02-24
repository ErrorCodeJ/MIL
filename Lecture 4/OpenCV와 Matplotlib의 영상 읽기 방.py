import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("lec7_candies.png")
img2 = plt.imread("lec7_candies.png")

cv2.imshow("opencv",img1)
cv2.imshow("plt", img2)
cv2.waitKey()