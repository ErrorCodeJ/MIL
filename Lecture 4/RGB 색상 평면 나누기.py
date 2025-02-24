src = cv2. imread('candies.png' , cv2.IMREAD_COLOR)

# 컬러 영상 속성 확인
print('src.shape:' , src.shape) # src.shape: (480, 640, 3)
print('src.dtype:' , src.dtype) # src.dtype: uint8

# RGB 색 평면 분할
b_plane, g_plane, r_plane = cv2.split(src)

cv2.imshow('src', src)
cv2.imshow('B_plane' , b_plane)
cv2.imshow('G_plane' , g_plane)
cv2.imshow('R_plane' , r_plane)