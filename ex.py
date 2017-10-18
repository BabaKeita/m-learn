import cv2
import sys
 
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print('OpenError')
    sys.exit()
 
cv2.namedWindow("demo", cv2.WINDOW_NORMAL)
face_cascade = cv2.CascadeClassifier('./traincascade/cascade/ooo/cas/cascade04_HaarALL.xml')
#/home/owner/anaconda3/conda-bld/src_cache/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_alt.xml
def function(frame):

    # グレースケール変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 検知
    faces = face_cascade.detectMultiScale(gray, 1.02)#1.21
    for (x,y,w,h) in faces:
        # 検知した顔を矩形で囲む
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        # 顔画像（グレースケール）
        roi_gray = gray[y:y+h, x:x+w]
        # 顔画像（カラースケール）
        roi_color = frame[y:y+h, x:x+w]

    return frame

while(True):
    ret, frame = cap.read()
 
    cv2.imshow('demo',function(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()
for i in range (1,5):
    cv2.waitKey(1)

