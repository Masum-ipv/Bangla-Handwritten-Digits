from flask import Flask, render_template, request
from sklearn.externals import joblib
import numpy as np
import re 
import nltk
from sklearn.naive_bayes import GaussianNB
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def main():
	if request.method == 'GET':
		return render_template('index.html')

	if request.method == 'POST':
		parameters = joblib.load('parameters.pkl')
		input_json = request.get_json(force=True) 
		print('data from client:', input_json)
		#answer = classifier.predict(x_tfid)
		print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		return "1"


if __name__ == "__main__":
	app.run(debug=True)
