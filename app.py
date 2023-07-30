from flask import Flask, request, jsonify, render_template
import pandas as pd

import joblib
from utils import preprocessor

app = Flask(__name__)
model = joblib.load('mymodel.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    input = request.form['text']
    predicted_sentiment = ???
    if predicted_sentiment == 1:
        output = 'positive'
    else:
        output = 'negative'

    return render_template(???, sentiment=f'Predicted sentiment of "{input}" is {output}.')


if __name__ == "__main__":
    app.run(debug=True)
