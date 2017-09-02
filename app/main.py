from flask import Flask, request
from util import classify_review

app = Flask(__name__)

REVIEW_PARAM='review'

# TO DO: all routes might start with /api/v0

@app.route("/classify", methods=['POST', 'GET'])
def classify():

    if request.method == 'GET':
        review = request.args.get(REVIEW_PARAM)
        return classify_review(review)
    elif request.is_json:
        review = request.get_json()[REVIEW_PARAM]
        return classify_review(review)
    else:
        # TO DO: throw a more officious / detailed exception
        return "bad request"

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=8000)
