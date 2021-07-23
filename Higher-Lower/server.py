from flask import Flask
import random

HIGHURL = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOWURL = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
ANSWERURL = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"


app = Flask(__name__)

correct_number = random.randint(0, 9)
print(correct_number)


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>'\
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200 />'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > correct_number:
        return '<h1>Guess is High</h1>'\
               f'<img src={HIGHURL} width=200>'
    elif guess < correct_number:
        return '<h1>Guess is Low</h1>'\
               f'<img src={LOWURL} width=200>'
    else:
        return '<h1>Guess is Correct</h1>'\
               f'<img src={ANSWERURL} width =200>'


if __name__ == '__main__':
    app.run(debug=True)
