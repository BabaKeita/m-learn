#11月14日火曜
#ドライブレコーダから標識を探すプログラム
#カスケードデータを2つ用意し,ひとつ目のデータで検出を行い、検出された画像をもうひとつのデータで確かめるコードを追加。

import cv2
import sys

# 自作Haar-like特徴分類器の読み込み
face_cascade = cv2.CascadeClassifier('./traincascade/cascade/ooo/cas/cascade06_LBPALL1.xml')
sign_cascade = cv2.CascadeClassifier('./traincascade/cascade/ooo/cas/cascade06_LBPALL1.xml')

# イメージファイルの読み込み
#img = cv2.imread('./img/signs02.jpg')
cap = cv2.VideoCapture('/home/owner/NORM2853.AVI')

if cap.isOpened() == False:
    print('OpenError')
    sys.exit()
cv2.namedWindow("demo", cv2.WINDOW_NORMAL)

def function(frame,m):
    i = 1
    # グレースケール変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 検知
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.01,minSize=(40,40),maxSize=(75,75))#1.21

    for (x,y,w,h) in faces:
        # 検知した部分を矩形で囲む
        dst = frame[y:y+h, x:x+w]
        if function2(dst) == 1:
            cv2.imwrite('./data/cv3'+ format(m) + '_' + format(i) + '.png',dst)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
        i += 1
    return frame

def function2(frame):
    j = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    signs = sign_cascade.detectMultiScale(gray, 1.01)#1.21
    for (x,y,w,h) in signs:
        # 検知した部分を矩形で囲む
        j = 1
    return j

n = 1
m = 1
while(True):
    ret, frame = cap.read()
    if ret == False:
        break
    # 画像表示
    if n == 7:
        cv2.imshow('demo',function(frame,m))
        n = 1
    n += 1
    m += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):#終了コマンド
        break
cap.release()
# 何かキーを押したら終了
cv2.waitKey(0)
cv2.destroyAllWindows()
