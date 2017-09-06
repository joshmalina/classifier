from sklearn.externals import joblib
import numpy as np

class Classification:

    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def classify_review(self, review_text):
        return self.model.predict(review_text)


class w2v():

    def __init__(self, path_to_vectors, dim=50):
        self.path = path_to_vectors
        self.w2v = {}
        self.inflate()
        assert(dim==len(self.w2v['the']))

    def inflate(self):
        with open(self.path, "r") as f:
            ls = f.readlines()
            for l in ls:
                parts = l.split(' ')
                word = parts[0]
                embedding = map(lambda x: float(x.replace('\n', '')), parts[1:])
                self.w2v[word] = np.array(list(embedding))

    def textToEmbMean(self, text):
        tokens = text.split(' ')
        mapped = [self.w2v[w] for w in tokens if w in self.w2v]
        if len(mapped) > 0:
            return np.mean(mapped, axis=0)
        else:
            return np.zeros(50)