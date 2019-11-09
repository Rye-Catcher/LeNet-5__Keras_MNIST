# LeNet-5__Keras_MNIST

### Introduction

> Implementation of LeNet-5 using Keras, and MNIST as training datasets. Able to identify handwritten digits

- LeNet-5    https://engmrk.com/lenet-5-a-classic-cnn-architecture/
- Keras      https://keras.io/
- MNIST of Handwritten digits     http://yann.lecun.com/exdb/mnist/

### How?

First make sure you have set up the environment

```
- pyhon
  - cv2
  - h5py
- TensorFlow
- Keras
```

Then run `python start.py`

It seems that running `start.exe` doesn't working and I have no idea how to solve it

Maybe I can code it in C++ and it is in the to-do list

OR

you can just run `train.py` to train your netral network

run `classify.py` to identify the number in `test.png`

### Notes

If you want to substitude `test.png`

Make sure it is `28*28` in pixel size

A simple to make one is to use your **mspaint**

### Acknowledgement

Inspired by https://blog.csdn.net/u014453898/article/details/97680748 and https://juejin.im/post/5d66b6725188257e99442108

For `cv2` functions, I learned them in https://www.kancloud.cn/aollo/aolloopencv/259610

And I use [pyinstaller](https://github.com/pyinstaller/pyinstaller) to convert `.py` file to `.exe`

Thanks my senior [@BoAi01](https://github.com/BoAi01) for his guidance and help
