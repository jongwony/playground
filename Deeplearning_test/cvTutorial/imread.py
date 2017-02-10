# -*- coding: utf-8 -*-

import numpy as np
import cv2

# cv2.IMREAD_COLOR = 1 : color image
# cv2.IMREAD_GRAYSCALE = 0 : gray image
# cv2.IMREAD_UNCHANGED = -1 : including alpha channel



img = cv2.imread('Jongwon.jpg', 0)

# 창에 이름과 옵션을 지정(옵션을 지정할 경우 창 생성후 이미지 로드)
# cv2.WINDOW_NORMAL = 창 resize 가능
# cv2.WINDOW_AUTOSIZE = default
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# display image
cv2.imshow('image', img)

# 키 입력 대기시간(ms) 0: 무한대
# 대기후 다음으로 넘어감
# 그전에 키가 입력되어도 다음으로 넘어감
k = cv2.waitKey(0) & 0xFF


if k == ord('s'):
    # save image
    cv2.imwrite('Jongwongray.png', img)

# 생성된 창 모두 파괴
cv2.destroyAllWindows()


