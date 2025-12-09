import numpy as np

class SearchEngine:
    def __init__(self, features_path, images_paths_path):
        self.features = np.load(features_path)
        self.images_paths = np.load(images_paths_path)

    def search(self, query_features, top_k=5):
        similarities = np.dot(self.features, query_features)

        indecies = np.argsort(similarities)[::-1][:top_k]

        results_paths = [str(self.images_paths[i]) for i in indecies]

        return results_paths
