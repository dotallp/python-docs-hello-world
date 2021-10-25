from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return ""

@app.route("/poc-3fe5d54dbf.html")
def about():
    return "Subdomain takeover by Chux"
