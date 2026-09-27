import os
from dotenv import load_dotenv

from flask import Flask, redirect, request, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from sqlalchemy import select

load_dotenv()

import models

#The "Template" and "Static" folders are assigned to match the project folder structure
app = Flask(__name__, template_folder="../Frontend/templates", static_folder="../Frontend/static")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
hasher = Bcrypt(app)
loginManager = LoginManager()
loginManager.init_app(app)

#Required function to allow Flask-Login to properly retrieve user account details
@loginManager.user_loader
def load_user(user_id):
    db = models.Session()
    try:
        user = db.get(models.User, int(user_id))
        return user
    finally:
        db.close()

#The Login page is the default page
@app.route("/")
def home():
    return redirect("/login")

#This route handles both rendering the login page, aaand handling login attempts
@app.route("/login", methods=["GET", "POST"])
def login():
    #"POST" requests hadnle users attempting to login
    if request.method == "POST":
        #Checks if there is the required data in the submitted form. If not, the login process is terminated and the Login page is refreshed.
        try:
            username = request.form["username"]
            password = request.form["password"]
        except:
            #TODO: Add proper error handling here
            print("Missing Data")
            return render_template("Login.html")
        db = models.Session()
        user = db.scalar(select(models.User).where(models.User.username == username))
        
        if user and hasher.check_password_hash(user.password, password):
            login_user(user)
            return redirect("/main-page")
        db.close()
    return render_template("Login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/Login")

@app.route("/main-page")
@login_required
def mainpage():
    return render_template("MainPage.html")

if __name__ == "__main__":
    app.run(debug=True)