from flask import Flask, render_template, request
from main import getResponseOfBot


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    userMessage = request.form["message"]

    reply = getResponseOfBot(userMessage)

    return reply


app.run(debug=True)