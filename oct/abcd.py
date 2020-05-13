import tensorflow.keras as tk
import pickle
import numpy as np
import matplotlib.pyplot as plt
import cv2

new_model = tk.models.load_model('../data/Final-4-conv,32-nodes,1-dense,1582188407')
# X_test = open('../data/X_test',"rb")
# Y_test = open('../data/y_test',"rb")
# X = pickle.load(X_test)
# X_test.close
# Y = pickle.load(Y_test)
# Y_test.close
# print(X[0])
# predictions = new_model.predict([X])
# CATEGORIES = ["CNV", "DME", "DRUSEN", "NORMAL"]
# print(CATEGORIES[np.argmax(predictions[2])])
# plt.imshow(X[2].reshape(80,80), cmap="gray")
# print(CATEGORIES[Y[2]])
# plt.show()

CATEGORIES = ["CNV", "DME", "DRUSEN", "NORMAL"]
X = []
IMG_SIZE = 80
img_array = cv2.imread('../media/oct_uploads/b.jpg', cv2.IMREAD_GRAYSCALE)
new_img = cv2.resize(img_array,(IMG_SIZE, IMG_SIZE))
# print(new_img)
X.append(new_img)
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
X = X/255.0
predictions = new_model.predict([X])
print(predictions[0])
print(CATEGORIES[np.argmax(predictions[0])])
plt.imshow(X[0].reshape(80,80), cmap="gray")

