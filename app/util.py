from pyfasttext import FastText

class Classification:

    def __init__(self, model_path):
        fasttext = FastText()
        self.model = fasttext.load_model(model_path)


    def classify_review(self, review_text):
        return self.model.predict_proba_single(review_text, k=1)[0]