#9月11日月曜
import cv2
 
# HOG特徴分類器の読み込み
face_cascade = cv2.HOGCascadeClassifier('./traincascade/cascade/ooo/cas/cascade05_HOG.xml')

# イメージファイルの読み込み
img = cv2.imread('./img/signs04.png')#04.jpg,04.png,02.jpg,05.png,06.png
 
# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 検知
faces = face_cascade.detectMultiScale(gray, 1.01)#1.21
for (x,y,w,h) in faces:
    # 検知した顔を矩形で囲む
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    # 顔画像（グレースケール）
    roi_gray = gray[y:y+h, x:x+w]
    # 顔画像（カラースケール）
    roi_color = img[y:y+h, x:x+w]

# 画像表示
cv2.imshow('img',img)
cv2.imwrite('data.png',img)
# 何かキーを押したら終了
cv2.waitKey(0)
cv2.destroyAllWindows()

