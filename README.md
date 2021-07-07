# :sleepy: Driver Drowsiness project python :sleeping:
This is a python project on driver drowsiness detection system.

<img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-%23F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" /><img alt="Keras" src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white"/><img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" /><img alt="NumPy" src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" /><img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/><img alt="OpenCV" src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"/><img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/><img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/><img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/><img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/><img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>

--------------------------

- As we know that many accidents happen because of driver's mistake where he has fallen asleep and :truck: accident occurs. So there is need for some system
which can detect and rings :loudspeaker: `alarm` when driver is drowsy.For this purpose , we can use this project as first step.In this project we have used
`keras` with tensorflow as backend for predicting about whether :eyes: are closed or open ,`openCV-python` for detecting eyes ,`pygame` for ringing alarm
and numpy and matplotlib for plotting and visualizing data.

- in this we have included jupyter notebook file `'dataset.ipynb'` which we have used for creating our dataset. It captures frames and detect left :eye: and right :eye:
using `haar xml files`, then save it to specified location.

- we have also included the `dataset` that we have created for training our model. We have three folders training images,validation images and test_images
in images folder. In each of three folders we have two folder closed and open which is used as label for our dataset. Our actual data resides in this
open and closed folders.

- In models folder, we have `myModel.h5` file which is our weight file for model.It is loaded into our main file for predictation of closed or open eyes.

- We have `'model.ipynb'` notebook file which contains code for our model creation , training and testing. it also contain code for data creation
and data visualization. More details are written inside the file.

- Then we have `'Driver Drowsiness Detection.ipynb'` file which is our main file. It contains code for the user interface and when to run alarm file
and predicting about whether driver is drowsy or not.

## Flask Api

----------------------------

```
link - https://driver-nidra-detection.herokuapp.com/
```
Input variables - preprossed image array of left and right eye

Cloud platform : heroku

## Django Webapp

----------------------------

<img src="https://github.com/arr-swartz/drowsiness_project_python/blob/master/screenshots/s1.png" width="600" height="400" />

<img src="https://github.com/arr-swartz/drowsiness_project_python/blob/master/screenshots/s2.png" width="600" height="400" />
