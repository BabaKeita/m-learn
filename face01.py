#8月30日水曜画像認識プログラム
import cv2
from matplotlib import pylab as plt

def face_detection(path):
    face_cascade = cv2.CascadeClassifier("/home/owner/anaconda3/conda-bld/src_cache/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("/home/owner/anaconda3/conda-bld/src_cache/opencv-3.1.0/data/haarcascades/haarcascade_eye.xml")

    img = cv2.imread(path)
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayed, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = grayed[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    print('aaa')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()


face_detection('test.png')

