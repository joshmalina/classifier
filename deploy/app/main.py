from flask import Flask, request
from util import Classification, w2v
#import os

app = Flask(__name__)

REVIEW_PARAM='review'

model_path = '../model.pkl'
glove_path = '../glove.6B.50d.txt'

classification = Classification(model_path)
w2v_ = w2v(glove_path)

# TO DO: all routes might start with /api/v0

@app.route("/classify", methods=['POST', 'GET'])
def classify():

    def process(review):
        review_as_vector = w2v_.textToEmbMean(review)
        return str(classification.classify_review(review_as_vector))

    if request.method == 'GET':
        review = request.args.get(REVIEW_PARAM)
        return process(review)
    elif request.is_json:
        review = request.get_json()[REVIEW_PARAM]
        return process(review)
    else:
        # TO DO: throw a more officious / detailed exception
        return "bad request"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
