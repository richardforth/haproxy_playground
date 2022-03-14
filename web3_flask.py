#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to web3.local!"

if __name__ == "__main__":
    app.run(port=5003)
