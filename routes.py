from app import app
from flask import render_template
import json
from urllib.request import urlopen

@app.route("/")
def index():

    url = "https://partnull.github.io/pizzapy/api.json"

    api = json.loads(urlopen(url).read().decode("utf-8"))

    result = api["articles"]

    return render_template("index.html", data=result)

