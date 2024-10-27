from flask import Flask, request, render_template

name = Flask(__name__, template_folder='templates', static_folder='assets')

@name.route("/")
def index():
    return render_template("index.html")

@name.route("/submit", methods=['POST'])
def submit():
    name = request.form['query']
    print(f'The query is {name}')
    return f"Your query has been received: {name}"

if __name__ == '__main__':
    name.run(debug=True)