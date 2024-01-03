from flask import Flask, render_template, request, jsonify
from chat import get_qa_chain

app = Flask(__name__)
chain = get_qa_chain()

@app.get("/")
def index_get():
    return render_template('base.html')

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = chain(text)['result']
    message = {"answer":response}

    return jsonify(message)

if __name__=="__main__":
    app.run(debug=True)

