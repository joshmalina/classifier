from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/classify", methods=['POST', 'GET'])
def classify():
  return request.values

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=80)
