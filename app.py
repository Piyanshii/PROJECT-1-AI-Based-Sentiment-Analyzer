from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

sentiment_pipeline = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        prediction = sentiment_pipeline(text)[0]

        label = prediction["label"]
        score = prediction["score"]

        result = {
            "text": text,
            "label": label,
            "score": round(score * 100, 2)
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
