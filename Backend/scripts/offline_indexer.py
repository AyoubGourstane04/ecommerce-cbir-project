import os
from PIL import Image
import numpy as np
from Backend.core.feature_extractor import FeatureExtractor

fe = FeatureExtractor()

image_folder = '../static/images'
feature_path = "../data/features.npy"
img_paths_path = "../data/image_paths.npy"

features = []
img_paths = []

print(f"Start indexing images from {image_folder}...")

for img_name in os.listdir(image_folder):
    if img_name.lower().endswith(('.jpg', '.png', '.jpeg')):
        try:
            img_path = os.path.join(image_folder, img_name)
            img = Image.open(img_path)
            feature = fe.extract(img)
            features.append(feature)
            img_paths.append(img_path)
            print(f"Indexed: {img_name}")
        except Exception as e:
            print(f"Error processing {img_name}: {e}")

np.save(feature_path, np.array(features))
np.save(img_paths_path, np.array(img_paths))

print(f"Done! Saved {len(features)} feature vectors to {feature_path}")