import keras
import cv2
import numpy as np
from keras.models import load_model

print("Using loaded model to predict...")
load_model = load_model("./lenet.h5")
img = cv2.imread('test.png',cv2.IMREAD_GRAYSCALE)
output=img.copy()

img = img.reshape(-1, 28, 28, 1)
img = img.astype('float32')

predicted = load_model.predict(img) #输出预测结果
print(predicted)
predicted = np.argmax(predicted)
print(predicted)

result="The Number Is {:d}".format(predicted)
output = cv2.resize(output, (512, 512))
cv2.putText(output, result, (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (155,155,0), 2)

cv2.imshow("img", output)
cv2.waitKey(0)