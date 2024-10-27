from flask import Flask, request, render_template
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

name = Flask(__name__, template_folder='templates', static_folder='assets')

@name.route("/")
def index():
    return render_template("index.html")

@name.route("/submit", methods=['POST'])
def submit():
    name = request.form['query']
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(name)
    print(f'The query is {name}')
    return f"Your query has been received: {response.text}"

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)

if __name__ == '__main__':
    name.run(debug=True)
    
    
    