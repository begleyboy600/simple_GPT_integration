from flask import Flask, render_template, request
import json
import os
import openai
import requests

with open("config/secrets.json") as config_file:
    config = json.load(config_file)

open_ai_secret_key = config.get("OPEN_AI_API_KEY")
openai.api_key = open_ai_secret_key

app = Flask(__name__)


@app.route("/")
def index():
    return "GPT-3 Playground"


@app.route("/interviewPrompt", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        job = request.form["job"]
        experience = request.form['experience']
        print(job)
        print(experience)

        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=f"Create a list of 8 questions for my interview as a {experience} {job}\n",
            temperature=0.5,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
        print("working")

        text = response.choices[0].text
        print(text)
        list = text.split('\n')[1:]
        list = filter(None, list)
        # list = ["sfsdgfsegds","sfsargsgd","sefsargsrgdsr"]
        return render_template("/interviewPrompt.html", list=list)
    else:
        return render_template("/interview.html")


if __name__ == "__main__":
    app.run(debug=True)
