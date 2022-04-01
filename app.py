import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_bootstrap import Bootstrap
from flask_session import Session
import keyboard
import csv

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

@app.route("/")
def home():
    print(guesses)
    return render_template("home.html", letter="_")
