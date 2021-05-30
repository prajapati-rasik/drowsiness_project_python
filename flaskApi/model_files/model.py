import cv2
import numpy as np
from keras.models import load_model


def predict(l_eye, r_eye):

    # loading our model
    model = load_model('model_files/modell.h5')
    rpred = [99]  # for taking class prediction of right eye
    lpred = [99]  # for taking class prediction of left eye

    rpred = model.predict_classes(r_eye)
    lpred = model.predict_classes(l_eye)

    if(rpred[0] == 0 and lpred[0] == 0):  # if both eyes are closed incerement the score
        return True
    else:  # if eyes are not closed decrement the score
        return False
