from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
response = requests.get("https://api.npoint.io/01415992a62b8bafe3fd").json()

@app.route("/")
def home():
    return render_template("./index.html", posts=response)

@app.route("/about")
def about():
    return render_template("./about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="isaac.ctd@gmail.com", password="dzauofhghfisuica")
            connection.sendmail(
                from_addr="isaac.ctd@gmail.com",
                to_addrs="isaac.ctd@gmail.com",
                msg=f"Subject: Someone contacted you on your website\n\n"
                    f"Name: {data['name']}\n"
                    f"Email: {data['email']}\n"
                    f"Phone: {data['phone']}\n"
                    f"Message: {data['message']}"
            )
        return render_template("contact.html", submitted=True)
    else:
        return render_template("contact.html", submitted=False)


@app.route("/post/<int:num>")
def blog_post(num):
    requested_post = None
    for post in response:
        if post["id"] == num:
            requested_post = post
    return render_template("./post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)
