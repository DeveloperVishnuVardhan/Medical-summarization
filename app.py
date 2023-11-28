from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load summarization model
summarizer = pipeline("summarization")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
