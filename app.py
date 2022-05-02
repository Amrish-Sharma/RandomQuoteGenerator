import requests
import json
import random
from flask import Flask

# variables
quote_url = 'https://raw.githubusercontent.com/Amrish-Sharma/FlipQuotes/83e1820ff6c33f17a7f9312389a45ff04e0917d1/app/src/main/assets/quotes.json'

# Flask app initialisation
app = Flask(__name__)

# randome quote page


@app.route("/rq")
def rqg():
    response = requests.get(quote_url).json()
    response_json = response['quotes']
    random_quote = random.choice(response_json)
    return random_quote

# index page


@app.route("/")
def index():
    return "<h1>Welcome to RandomQuoteGenerator<h2>"


if __name__ == "__main__":
    app.run(debug=True)
