from flask import Flask, request, render_template
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

app = Flask(__name__, template_folder='templates', static_folder='assets')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    name = request.form['query']
    model = genai.GenerativeModel("gemini-1.5-flash")
    query_response = model.generate_content(name)
    query_example = f"Based on this explanation: {query_response.text}, provide a relevant example."
    query_example_response = model.generate_content(query_example)
    return render_template("index.html", explanation=query_response.text, example=query_example_response.text)

# return f"Your query has been received: {response.text}"
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)

if __name__ == '__main__':
    app.run()
    
    
    