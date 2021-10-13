from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return ""

@app.route("/poc")
def about():
    return "Subdomain takeover POC by Chux"
