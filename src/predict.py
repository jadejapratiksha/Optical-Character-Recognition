import matplotlib.pyplot as plt
from keras.models import load_model
import cv2
import numpy as np

model = load_model('Model/model.h5')
img=cv2.imread('nhcd/1/001_01.jpg',0)
ret,seg = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
fig=plt.figure()
ax1=fig.add_subplot(1,2,1)
plt.imshow(img,cmap='gray')
ax1.title.set_text('Orignal')
ax3=fig.add_subplot(1,2,2)
plt.imshow(seg,cmap='gray')
ax3.title.set_text('Segmented')
plt.show()
fr = np.array(seg)
fr = fr.reshape(1, 28, 28, 1)
fr = fr.astype('float32') / 255

clas=model.predict_classes(fr)
print("Class is",int(clas))