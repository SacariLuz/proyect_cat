#!/usr/bin/python3
"""
App creacion
"""

from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/cats")
def cats():
    cat_api_url = " https://api.thecatapi.com/v1/images/search?limit=10"
    images = requests.get(cat_api_url).json()
    return render_template("cats.html", images=images)


@app.route("/motivacion")
def motivacion():
    motivacion_api_url = "https://type.fit/api/quotes"
    frases = requests.get(motivacion_api_url).json()
    return render_template("motivacion.html", frases=frases)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
