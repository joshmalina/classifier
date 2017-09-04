from flask import Flask, request
from util import Classification
import os

app = Flask(__name__)

REVIEW_PARAM='review'

classification = Classification(os.environ['MODEL'])

# TO DO: all routes might start with /api/v0

@app.route("/classify", methods=['POST', 'GET'])
def classify():

    if request.method == 'GET':
        review = request.args.get(REVIEW_PARAM)
        return classification.classify_review(review)
    elif request.is_json:
        review = request.get_json()[REVIEW_PARAM]
        return classification.classify_review(review)
    else:
        # TO DO: throw a more officious / detailed exception
        return "bad request"

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=8000)
