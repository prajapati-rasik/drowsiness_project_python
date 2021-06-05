#from keras.models import load_model
import queue
from imutils.video import VideoStream
import imutils
import requests
import playsound
import cv2
import os
import numpy as np
from django.conf import settings
import numpy as np
import time
import threading

face = cv2.CascadeClassifier(
    'nidra/haar_cascade/haarcascade_frontalface_alt.xml')
leye = cv2.CascadeClassifier(
    'nidra/haar_cascade/haarcascade_lefteye_2splits.xml')
reye = cv2.CascadeClassifier(
    'nidra/haar_cascade/haarcascade_righteye_2splits.xml')

model = load_model('nidra/model/myModel.h5')  # loading our model

font = cv2.FONT_HERSHEY_COMPLEX_SMALL  # font style for putting text on frame

myQueue = queue.Queue()


def storeInQueue(f):
    def wrapper(*args):
        myQueue.put(f(*args))
    return wrapper


class VideoCamera(object):
    def __init__(self, useApi):
        self.vs = VideoStream(src=0).start()
        if self.vs:
            print("camera accessed")
        self.cnt = 0  # counting frames for api
        self.aapi = useApi  # flag for deciding whether to use model or api
        self.score = 0  # if score goes greater than 15 then ring the alarm
        self.thicc = 2
        self.download_thread = None
        if useApi == 1:
            self.threshold = 2
        else:
            self.threshold = 15

    def __del__(self):
        cv2.destroyAllWindows()
        self.vs.stop()

    def detect_and_predict_eyes_using_model(self, frame):

        height, width = frame.shape[:2]

        # converting frame to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # now we detect face , left_eye and right_eye , see dataset.ipynb for more information
        faces = face.detectMultiScale(
            gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25))
        left_eye = leye.detectMultiScale(gray)
        right_eye = reye.detectMultiScale(gray)

        rpred = [99]  # for taking class prediction of right eye
        lpred = [99]  # for taking class prediction of left eye

        for (x, y, w, h) in right_eye:
            r_eye = frame[y:y + h, x:x + w]  # extracting right eye from frame
            # converting to gray scale
            r_eye = cv2.cvtColor(r_eye, cv2.COLOR_BGR2GRAY)
            # resizing image to (24,24) which input size for our model
            r_eye = cv2.resize(r_eye, (24, 24))
            r_eye = r_eye / 255
            r_eye = r_eye.reshape(24, 24, -1)
            r_eye = np.expand_dims(r_eye, axis=0)
            rpred = model.predict_classes(
                r_eye)  # it will predict the class of the image means either eye is open or closed
            # if it gives 1 then eye is open because 1 is assigned to open (check model.ipynb)
            if rpred[0] == 1:
                lbl = 'Open'  # set label to open
            if rpred[0] == 0:  # if it gives 0 then eye is closed bacause 0 is assigned to closed
                lbl = 'Closed'  # set label to closed
            break

        for (x, y, w, h) in left_eye:
            l_eye = frame[y:y + h, x:x + w]  # extracting left eye from frame
            # converting to gray scale
            l_eye = cv2.cvtColor(l_eye, cv2.COLOR_BGR2GRAY)
            l_eye = cv2.resize(l_eye, (24, 24))  # resizing image
            l_eye = l_eye / 255
            l_eye = l_eye.reshape(24, 24, -1)
            l_eye = np.expand_dims(l_eye, axis=0)
            lpred = model.predict_classes(l_eye)
            # if it gives 1 then eye is open because 1 is assigned to open (check model.ipynb)
            if lpred[0] == 1:
                lbl = 'Open'  # set label to open
            if lpred[0] == 0:  # if it gives 0 then eye is closed bacause 0 is assigned to closed
                lbl = 'Closed'  # set label to closed
            break

        if rpred[0] == 0 and lpred[0] == 0:
            return (faces, True)
        else:
            return (faces, False)
        return (faces, False)

    def detect_and_predict_eyes_using_api(self, frame):

        height, width = frame.shape[:2]

        # converting frame to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # now we detect face , left_eye and right_eye , see dataset.ipynb for more information
        faces = face.detectMultiScale(
            gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25))
        left_eye = leye.detectMultiScale(gray)
        right_eye = reye.detectMultiScale(gray)

        self.cnt += 1
        if self.cnt % 60 != 0:
            return (faces, None)
        else:
            self.cnt = 1
        if self.download_thread is not None:
            if self.download_thread.is_alive():
                return (faces, None)
        self.download_thread = threading.Thread(
            target=self.function_that_do, name="worker", args=[left_eye, right_eye, frame])
        self.download_thread.start()

        if myQueue.qsize() == 0:
            return (faces, None)
        response = myQueue.get()
        return (faces, False)

    @storeInQueue
    def function_that_do(self, left_eye, right_eye, frame):
        l_eye = np.zeros((24, 24))
        r_eye = np.zeros((24, 24))
        for (x, y, w, h) in right_eye:
            r_eye = frame[y:y + h, x:x + w]  # extracting right eye from frame
            # converting to gray scale
            r_eye = cv2.cvtColor(r_eye, cv2.COLOR_BGR2GRAY)
            # resizing image to (24,24) which input size for our model
            r_eye = cv2.resize(r_eye, (24, 24))
            r_eye = r_eye / 255
            r_eye = r_eye.reshape(24, 24, -1)
            r_eye = np.expand_dims(r_eye, axis=0)
            break

        for (x, y, w, h) in left_eye:
            l_eye = frame[y:y + h, x:x + w]  # rxtracting left eye from frame
            # converting to gray scale
            l_eye = cv2.cvtColor(l_eye, cv2.COLOR_BGR2GRAY)
            l_eye = cv2.resize(l_eye, (24, 24))  # resizing image
            l_eye = l_eye / 255
            l_eye = l_eye.reshape(24, 24, -1)
            l_eye = np.expand_dims(l_eye, axis=0)
            break

        reqq = {
            'left_eye': l_eye.tolist(),
            'right_eye': r_eye.tolist()
        }

        url = " https://driver-nidra-detection.herokuapp.com/"
        response = requests.post(url, json=reqq)
        response.text.strip()
        flag = response.text[12:16] == "true"
        return flag, flag

    def get_frame(self):
        frame = self.vs.read()
        frame = imutils.resize(frame, width=650)
        frame = cv2.flip(frame, 1)

        height, width = frame.shape[:2]

        if self.aapi == 1:
            (faces, isclosed) = self.detect_and_predict_eyes_using_api(frame)
        else:
            (faces, isclosed) = self.detect_and_predict_eyes_using_model(frame)

        # drawing rectangle of frame size
        cv2.rectangle(frame, (0, height - 70), (210, height),
                      (0, 255, 0), thickness=cv2.FILLED)

        # drawing rectangle around the face where x and y are coordinates of upper left
        for (x, y, w, h) in faces:
            # corner, w=width, h-height
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

        if isclosed is None:
            if self.score > 2:
                cv2.putText(frame, "sleep", (10, height - 20),
                            font, 1.1, (0, 0, 0), 2, cv2.LINE_AA)
            else:
                cv2.putText(frame, "awake", (10, height - 20),
                            font, 1.1, (0, 0, 0), 2, cv2.LINE_AA)
        elif isclosed:  # if both eyes are closed increment the score
            self.score = self.score + 1
            cv2.putText(frame, "Closed", (10, height - 20),
                        font, 1.1, (0, 0, 0), 2, cv2.LINE_AA)
            # it will put the text closed in frame, we have given coordinated of upper left corner of block,
            # font type,color,line type
        else:  # if eyes are not closed decrement the score
            self.score = self.score - 1
            cv2.putText(frame, "Open", (10, height - 20),
                        font, 1.1, (0, 0, 0), 2, cv2.LINE_AA)

        if self.score < 0:  # restricting our score not to go less than zero
            self.score = 0
        cv2.putText(frame, 'Score:' + str(self.score), (100, height - 20), font, 1.1, (0, 0, 0), 2,
                    cv2.LINE_AA)  # putting score to frame
        if self.score > self.threshold:
            # person is feeling sleepy so we beep the alarm
            try:
                playsound("sounds/alarm.wav")  # playing alarm file
            except:  # isplaying = False
                pass
            if self.thicc < 16:  # this is for displaying motion of borders when alarm beeps
                self.thicc = self.thicc + 2
            else:
                self.thicc = self.thicc - 2
                if self.thicc < 2:
                    self.thicc = 2
            cv2.rectangle(frame, (0, 0), (width, height),
                          (0, 0, 255), self.thicc)  # drawing rectangle

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
