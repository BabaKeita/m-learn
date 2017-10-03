#9月11日水曜画像認識プログラム
import cv2
from matplotlib import pylab as plt

def dog_detection(path):
    dog_cascade = cv2.CascadeClassifier("./traincascade/cascade/ooo/cascade.xml")

    img = cv2.imread(path)
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dog = dog_cascade.detectMultiScale(grayed, 1.3, 5)
    for (x, y, w, h) in dog:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = grayed[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

dog_detection('img/signs02.jpg')
cv2.waitKey(0)
cv2.destroyAllWindows()
