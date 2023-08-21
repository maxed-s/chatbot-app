from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import chatbot_model


# response = openai.Completion.create(
#     model = "text-davinci-003",
#     prompt = "",
#     temperature=0.7,
#     max_tokens=256,
#     top_p = 1,
#     frequency_penalty=0,
#     presence_penalty = 0
# )


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods=["GET", "POST"])
def api():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        answer = chatbot_model.run_model(question)
        index = answer.find('Question');
        ind = slice(index)
        data = {"result": f"{answer[ind]}"}
        return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}
    return jsonify(data)

@app.route("/createaccount", methods=["GET", "POST"])
def createaccount():
    if request.method == "POST":
        task = request.json.get("")
        return task
    dat = ""
    return dat

app.run(debug = True, port = 5000)