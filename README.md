# :sleepy: Driver Drowsiness project python :sleeping:
this is a python project on driver drowsiness detection system

### :man_student: creator :- 
* Rasik Prajapati 
* Niraj Prajapati

> As we know that many accidents happen because of driver's mistake where he has fallen asleep and :truck: accident occurs. So there is need for some system
which can detect and rings :loudspeaker: `alarm` when driver is drowsy.For this purpose , we can use this project as first step.In this project we have used
`keras` with tensorflow as backend for predicting about whether :eyes: are closed or open ,`openCV-python` for detecting eyes ,`pygame` for ringing alarm
and numpy and matplotlib for plotting and visualizing data.

> in this we have included jupyter notebook file `'dataset.ipynb'` which we have used for creating our dataset. It captures frames and detect left :eye: and right :eye:
using `haar xml files`, then save it to specified location.

> we have also included the `dataset` that we have created for training our model. We have three folders training images,validation images and test_images
in images folder. In each of three folders we have two folder closed and open which is used as label for our dataset. Our actual data resides in this
open and closed folders.

> In models folder, we have `myModel.h5` file which is our weight file for model.It is loaded into our main file for predictation of closed or open eyes.

> We have `'model.ipynb'` notebook file which contains code for our model creation , training and testing. it also contain code for data creation
and data visualization. More details are written inside the file.

> Then we have `'Driver Drowsiness Detection.ipynb'` file which is our main file. It contains code for the user interface and when to run alarm file
and predicting about whether driver is drowsy or not.

## Flask Api

link - ` https://driver-nidra-detection.herokuapp.com/`
input variables - preprossed image array of left and right eye

Cloud platform : heroku
