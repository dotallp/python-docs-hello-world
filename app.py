from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return ""

@app.route("/poc")
def about():
    return "<h3>Subdomain takeover POC by Chux</h3>"
