from flask import Flask, render_template, request
from langchain.llms import Cohere

app = Flask(__name__)
cohere = Cohere(model='command-xlarge')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generative-ai', methods=['POST'])
def predict():
    text = request.form['text']
    response = cohere(text)
    return render_template('index.html', text=text, response=response)

if __name__ == '__main__':
    app.run(debug=True)
