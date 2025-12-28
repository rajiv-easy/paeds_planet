from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# Render uses Gunicorn, so no app.run() needed
