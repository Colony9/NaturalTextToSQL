from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return redirect

@app.route("/login")
def login():
    return "TODO"

@app.route("/logout")
def logout():
    return "TODO"

@app.route("/main-page")
def mainpage():
    return "TODO"

if __name__ == "__main__":
    app.run()