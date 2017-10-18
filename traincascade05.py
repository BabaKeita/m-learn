import cv2
import numpy as np

# 学習器(cascade.xml)の指定
Cascade = cv2.CascadeClassifier('./traincascade/cascade/ooo/cas/cascade04_HaarALL.xml')
# 予測対象の画像の指定
img = cv2.imread('./img/signs02.jpg', cv2.IMREAD_COLOR)#04.jpg,04.png,02.jpg,05.png,06.png
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
point = Cascade.detectMultiScale(gray, 1.01, 3)

if len(point) > 0:
    for rect in point:
        cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=2)
else:
    print("no detect")

cv2.imwrite('detected.jpg',img)
cv2.imshow('detected.jpg', img)

# 何かキーを押したら終了
cv2.waitKey(0)
cv2.destroyAllWindows()
