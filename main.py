import os
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup


app = Flask(__name__)


template = """<a href={}>A Random Fact in Pig Latin</a>"""
url = 'http://hidden-journey-62459.herokuapp.com/piglatinize/'


def get_fact():
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    return facts[0].getText()


def get_pig_latin(the_fact):
    payload = {'input_text': the_fact}
    response = requests.post(url ,data=payload, allow_redirects=False)
    return response


@app.route('/')
def home():
    the_fact = get_fact().strip()
    pig_latin = get_pig_latin(the_fact)
    return template.format(pig_latin.headers['location'])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
