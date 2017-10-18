#10月4日水曜
#ドライブレコーダから標識を探すプログラム
import cv2
import sys

# 自作Haar-like特徴分類器の読み込み
face_cascade = cv2.CascadeClassifier('./traincascade/cascade/ooo/cas/cascade06_HAAR.xml')

# イメージファイルの読み込み
#img = cv2.imread('./img/signs02.jpg')
cap = cv2.VideoCapture('/home/owner/NORM2853.AVI')

if cap.isOpened() == False:
    print('OpenError')
    sys.exit()
cv2.namedWindow("demo", cv2.WINDOW_NORMAL)

def function(frame):

    # グレースケール変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 検知
    faces = face_cascade.detectMultiScale(gray, 1.01)#1.21
    for (x,y,w,h) in faces:
        # 検知した顔を矩形で囲む
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        # 顔画像（グレースケール）
        roi_gray = gray[y:y+h, x:x+w]
        # 顔画像（カラースケール）
        roi_color = frame[y:y+h, x:x+w]

    return frame
n = 1
while(True):
    ret, frame = cap.read()
    if ret == False:
        break
    # 画像表示
    if n == 7:
        cv2.imshow('demo',function(frame))
        n = 1
    n += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):#終了コマンド
        break
cap.release()
# 何かキーを押したら終了
cv2.waitKey(0)
cv2.destroyAllWindows()

