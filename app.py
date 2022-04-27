# An app by Tim Shaw

import os

from flask import Flask, flash, jsonify, make_response, redirect, render_template, request, session
from flask_bootstrap import Bootstrap
from flask_session import Session
import keyboard
import csv
import random

import recommend_words as rw

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

# https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file
with open('wordle_frequencies.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('wordle_frequencies2.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        word_frequencies = {rows[0]:rows[1] for rows in reader}

# Function to split word into list of letters
def split(word):
    return [char for char in word]

# Function to generate the word to guess
def generate_solution():
    # Choose random solution and store in array
    global solution, solution_list, solution_dict, temp_solution_dict, valid_guesses, valid_letters, invalid_letters, letter_indices, g
    solution = random.choice(solutions)
    solution = solution.upper()
    solution_list = split(solution)

    # Generate a dictionary for each letter of the alphabet
    solution_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    # Count how many times each letter is in the word
    for letter in solution:
        solution_dict[letter] += 1
    # Store copy of original dictionary
    temp_solution_dict = solution_dict.copy()

    # List to store valid guesses
    valid_guesses = []
    
    # List to store valid letters
    valid_letters = []

    # List to store invalid letters
    invalid_letters = []

    # Dict to store letter indexes
    letter_indices = {}

    g = []

    reset_valid_guesses()

def reset_valid_guesses():
    # List to store valid guesses
    valid_guesses.clear()
    g.clear()
    for guess in guesses:
        valid_guesses.append(guess)
        g.append(guess)
    for solution in solutions:
        valid_guesses.append(solution)
        g.append(solution)

    valid_letters.clear()
    invalid_letters.clear()
    letter_indices.clear()



generate_solution()

# List to store green/yellow/gray letters
colors = ['gray', 'gray', 'gray', 'gray', 'gray']
temp_colors = ['gray', 'gray', 'gray', 'gray', 'gray']

win = ['green', 'green', 'green', 'green', 'green']

start_guess = rw.recommend_words(valid_guesses, valid_letters, invalid_letters, g, word_frequencies)

def game(word):
    word = word.upper()
    word_list = split(word)

    # Check for green letters
    for i in range(5):
        if word_list[i] == solution_list[i]:
            colors[i] = 'green'
            # Decrement count
            solution_dict[solution_list[i]] -= 1
            valid_letters.append(word_list[i]) if word_list[i] not in valid_letters else None

            if word_list[i] not in letter_indices:
                letter_indices[word_list[i]] = [i]
            elif i not in letter_indices[word_list[i]]:
                letter_indices[word_list[i]].append(i)

    # Check for yellow letters
    for i in range(5):
        for j in range(5):
            # if we haven't checked the letter already, and if it is in the word, make it yellow
            if solution_dict[word_list[i]] > 0 and word_list[i] == solution_list[j] and colors[i] == 'gray':
                colors[i] = 'gold'
                solution_dict[word_list[i]] -= 1
                valid_letters.append(word_list[i]) if word_list[i] not in valid_letters else None

                # If we have a letter in the wrong place, store it's index as negative
                if word_list[i] not in letter_indices:
                    letter_indices[word_list[i]] = [-(i+1)]
                elif i not in letter_indices[word_list[i]]:
                    letter_indices[word_list[i]].append(-(i+1))

    # Add gray letters to invalid letters
    for letter in word_list:
        if letter not in valid_letters:
            invalid_letters.append(letter) if letter not in invalid_letters else None


    # remove words with invalid letters
    rw.remove_words(valid_guesses, invalid_letters, valid_letters, letter_indices, word_frequencies)
    # Get top 10 words to guess
    global top_10
    top_10 = rw.recommend_words(valid_guesses, valid_letters, invalid_letters, g, word_frequencies)

    # Don't recommend a word we have already guessed
    if word.lower() in valid_guesses:
        valid_guesses.remove(word.lower()) 

    
    # Reset colors to gray
    for i in range(5):
        temp_colors[i] = colors[i]
        colors[i] = 'gray'
    
    # Reset dict to original dictionary
    solution_dict.clear()
    solution_dict.update(temp_solution_dict)

    if word == solution:
        # If we win, change the solution 
        # Word will be different upon refresh
        generate_solution()

def test():
    word1 = start_guess[0]
    count = 1
    while word1 != solution.lower():
        game(word1)
        if len(valid_guesses) == 0 or count > 6:
            print("FAIL")
            count += 1
            return 7
        if len(valid_guesses) < 10:
            word1 = valid_guesses[0]
        else:
            word1 = top_10[0]
        count += 1
    return count
'''
totals = 0
count1 = 0
for i in range(100):
    totals += test()
    count1 += 1
    generate_solution()

print(totals/count1)
'''

# Server stuff
@app.route("/", methods=['POST', 'GET'])
def home():

    if request.method == 'GET':
        generate_solution()

    # Get guess from page
    if request.method == "POST":
        guess = request.get_json()
        # If we lose
        if guess == "loss":
            res = make_response({"solution": solution}, 200)
            # Generate a new solution after sending the old answer to the web page
            generate_solution()
            return res
        # Check the word
        game(guess)

        # Check for valid response
        if guess.lower() not in guesses and guess.lower() not in solutions:
            res = make_response({"message": "invalid"}, 200)
        # Check for win
        elif colors == win:
            res = make_response({"message": "win"}, 200)
            generate_solution()
        # Send back colors
        else:
            # If our recommendations are poor, return valid guesses
            if len(valid_guesses) < 10:                    
                res = make_response({"message": temp_colors, "top_10": valid_guesses}, 200)
            else:
                res = make_response({"message": temp_colors, "top_10":top_10}, 200)
        return res
    return render_template("home.html")
