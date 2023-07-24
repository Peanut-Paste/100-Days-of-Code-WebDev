from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    random_number = random.randint(1, 10)
    current_year = datetime.today().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<name>")
def inputname(name):
    response_agify = requests.get("https://api.agify.io/", params={"name": name})
    agify_data = response_agify.json()
    response_genderization = requests.get("https://api.genderize.io", params={"name": name})
    genderization = response_genderization.json()
    return render_template("input_name.html", name=name, age=agify_data["age"], gender=genderization["gender"])


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/5e7bcc87189d2b54544c")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


