from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html", name="Isaac")

@views.route("/profile")
def profile():
    return "Profile"
