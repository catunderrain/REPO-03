import os
import cv2
import os
import time
import uuid
import shutil

IMAGES_PATH = 'c:\\noirecode\\python\\projectsb\\handsigns\\files\\imgs'
try:
    shutil.rmtree(IMAGES_PATH)
    os.mkdir(IMAGES_PATH)
except:
    os.mkdir(IMAGES_PATH)

labels = ['hello', 'bye']
number_imgs = 10
for label in labels:
    os.mkdir(IMAGES_PATH + '\\' + label)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(
            IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        print(imgname)
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
