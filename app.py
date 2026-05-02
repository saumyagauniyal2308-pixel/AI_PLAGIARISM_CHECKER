from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/check", methods=["POST"])
def check_plagiarism():
    file1 = request.files["file1"]
    file2 = request.files["file2"]

    text1 = file1.read().decode("utf-8", errors="ignore")
    text2 = file2.read().decode("utf-8", errors="ignore")

    words1 = [w for w in text1.lower().split() if w.isalnum()]
    words2 = [w for w in text2.lower().split() if w.isalnum()]

    plag_words = len(set(words1).intersection(set(words2)))
    total_words = len(words1) + len(words2)

    plag_percent = 100 - round((total_words - plag_words*2)/total_words*100)

    return jsonify({"percentage": plag_percent})

if __name__ == "__main__":
    app.run(debug=True)