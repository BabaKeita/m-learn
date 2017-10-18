#10月11日水曜
#ドライブレコーダから標識を探すプログラム
#検出された画像をdataディレクトリに保存する
#10月17日火曜
#テキストファイルにnegファイル名を記録する際にディレクトリのパスを追加しやすくした。
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

def function(frame, m):
    i = 1
    # グレースケール変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 検知
    faces = face_cascade.detectMultiScale(gray, 1.01)#1.21
    for (x,y,w,h) in faces:
        # 検知した部分を矩形で囲む
        dst = frame[y:y+h, x:x+w]
        cv2.imwrite('./data/cv1_'+ format(m) + '_' + format(i) + '.png',dst)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
        i += 1
    return frame

n = 1
m = 1
while(True):
    ret, frame = cap.read()
    if ret == False:
        break
    # 画像表示
    if n == 7:
        cv2.imshow('demo',function(frame, m))
        n = 1
    n += 1
    m += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):#終了コマンド
        break
cap.release()
# 何かキーを押したら終了
cv2.waitKey(0)
cv2.destroyAllWindows()

