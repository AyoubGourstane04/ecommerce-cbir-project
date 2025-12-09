from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.models import Model
import numpy as np


class FeatureExtractor : 
    def __init__(self):
        base_model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')
        self.model = Model(inputs =  base_model.inputs, outputs = base_model.outputs)

    def extract(self, img):
        img = img.resize((224, 224))
        x = image.img_to_array(img)
        x= np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        features = self.model.predict(x)[0]

        return features / np.linalg.norm(features)
