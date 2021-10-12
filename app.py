from flask import Flask
app = Flask(__name__)

@app.route("/poc.html")
def hello():
    return "Subdomain takeover POC by Chux"
