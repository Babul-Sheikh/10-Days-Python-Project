#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Resume</h1><p>Name: Your Name</p><p>Role: Developer</p>"

@app.route("/about")
def about():
    return "<h1>About</h1><p>Simple Flask app serving plain HTML.</p>"

if __name__ == "__main__":
    app.run()  # simple default server

