from flask import Flask, render_template
import requests


app = Flask(__name__)

response = requests.get("https://api.npoint.io/5e7bcc87189d2b54544c")
all_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:blog_num>')
def post(blog_num):
    return render_template("post.html", num=blog_num, posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
