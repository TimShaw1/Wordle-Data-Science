import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_bootstrap import Bootstrap
from flask_session import Session
import keyboard
import csv
import random

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Data retrieved from https://www.kaggle.com/datasets/bcruise/wordle-valid-words?resource=download&select=valid_solutions.csv
# Code referenced from https://stackoverflow.com/questions/24662571/python-import-csv-to-list 
# Store wordle datasets
with open('valid_solutions.csv', newline='') as f:
    reader = csv.reader(f)

    # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
    # this makes the data a list instead of a list of lists
    flat_list = [item for sublist in reader for item in sublist]

    solutions = list(flat_list)

with open('valid_guesses.csv', newline='') as f:
    reader = csv.reader(f)

    # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
    # this makes the data a list instead of a list of lists
    flat_list = [item for sublist in reader for item in sublist]

    guesses = list(flat_list)

# Choose random solution and store in array
solution = random.choice(solutions)
solution = solution.upper()
solution_list = solution.split()

# List to store green/yellow/gray letters
colors = [0,0,0,0,0]

solution = "GREEN"


def game(word):

    word = word.upper()

    if word == solution:
        print("Win")

    print(solution)
    count = 0
    for guess_letter in word:
        if guess_letter in solution:
            if guess_letter == solution[count]:
                colors[count] = 'green'
            else:
                colors[count] = 'yellow'
        else:
            colors[count] = 'gray'

        count += 1

    

@app.route("/", methods=['POST', 'GET'])
def home():

    # Get guess from page
    if request.method == "POST":
        guess = request.get_json()
        game(guess)
        print(colors)

    return render_template("home.html")
