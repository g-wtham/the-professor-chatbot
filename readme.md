# The Professor Chatbot

### Layman to Einstein-level explanation at your fingertips!

Everytime you ask a concept to chatbot, it gonna confuse you with an explanation that's way out of your understanding or too simple to be useless. Turns out that I can solve our universal issue!

Simply, adjust the slider based on your desired level of explanation (1 - Kudos babyy!; 5 - Hello, Einstein!). Everything inbetween acts as side-characters with **SIMPLE** to **MEDIUM** level explanations.

Not just **explanations**, pairing it up with **example**, so you can wrap the concept around your head better this time than smashing the keyboard once again, bombing chatgpt with your vocabulary skills!
**LEAVEMEALONE - CHEAT ACTIVATED for CHATGPT**

Enough of marketing, just use it here : https://the-professor-chatbot.onrender.com/
Alternative link : https://summer-limit-8069.ploomber.app/

## Features:

1. Explanation & Example gets generated each time
2. Easy on your device, not yet another overengineered website, pure html & css only!

## Technologies Used:

1. HTML, CSS, Python (yes, you seen it right, its not JS, its PYTHON🐍)
2. Flask
3. Gemini API (Latest Model)
4. Render (for hosting the flask server online)

## Wish to use on your local machine?

1. Clone the repository (https://github.com/g-wtham/the-professor-chatbot)
2. Locate the root directory and open CMD in this path.
3. Type ``pip install -r requirements.txt``. This will install all the required packages needed to run this on your local machine
   [flask, google-generativeai, python-dotenv, gunicorn (for production server)]
4. Now, you need to get an API Key to use your own Gemini API, create a new file named **.env**, add this into the file ``export GEMINI_API_KEY=your_api_key_here``, replace with your api key.
5. Go to ``(https://aistudio.google.com/app/apikey)`` to get your own gemini api key, which can be tracked in your google cloud console. No worries, there's some free api limit, enjoy!
6. After replacing the api key, now go to the root directory in cmd of this project, type in the command ``flask run`` to start your local flask server or run this ``python app.py``
7. You will now have your own local version of this project running at ``http://127.0.0.1:5000/``.
8. Don't forget to Ctrl+C to end your flask server service, but never stop hitting Ctrl+C as a dev😛
