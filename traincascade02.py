#9月11日月曜
#10月11日水曜更新検知された部分を画像ファイルとしてdataディレクトリに保存
import cv2
 
# 自作Haar-like or LBP特徴分類器の読み込み
face_cascade = cv2.CascadeClassifier('./traincascade/cascade/ooo/cas/cascade05_HaarALL.xml')

# イメージファイルの読み込み
img = cv2.imread('./img/signs06.png')#04.jpg,04.png,02.jpg,05.png,06.png
 
# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 検知
faces = face_cascade.detectMultiScale(gray, 1.01)#1.21
i = 1
for (x,y,w,h) in faces:
    # 検知した部分を矩形で囲む
    dst = img[y:y+h, x:x+w]
    cv2.imwrite('./data/data'+ format(i) + '.png',dst)    
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
    # 画像（グレースケール）
#    roi_gray = gray[y:y+h, x:x+w]
    # 画像（カラースケール）
#    roi_color = img[y:y+h, x:x+w]
    i += 1

# 画像表示
cv2.imshow('img',img)
#cv2.imwrite('data.png',img)
# 何かキーを押したら終了
cv2.waitKey(0)
cv2.destroyAllWindows()

