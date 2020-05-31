import os

from ujimaru_markov_model import Ujimaru

from flask import Flask

app = Flask(__name__)
ujimaru = Ujimaru()


@app.route("/")
def generate():
    return ujimaru.make_sentence()


@app.route("/tweet")
def tweet():
    return ujimaru.make_tweet()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
