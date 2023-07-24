from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def main_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


random_no = random.randint(0, 9)

@app.route("/<int:number>")
def chosen_number(number):
    if number < random_no:
        return "<h1 style='color:red'>Too low!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    elif number > random_no:
        return "<h1 style='color:blue'>Too high!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

    else:
        return "<h1 style='color:green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)