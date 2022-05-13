# Tim Shaw's Wordle Solver
#### Video Demo: https://youtu.be/DUz53uftLZ0
#### Description:
Created by Tim Shaw for CS50

A simple web app with flask and javascript that simulates a game of wordle. I created a backend to run the gameplay of the game, while the frontend serves as a nice user interface.

The app works by sending a word from the website via a POST response after validation. The server gets the guessed word and compares it to the solution. Then, the server responds to the website with the colors to be displayed. If a user guesses the word correctly, the server tells the website to display all green!

This app also uses an algorithm I wrote to recommend words to the user. This works by determining a list of possible solutions, then determining which word should be guessed next to maximise the chance of success. The algorithm accounts for letter frequency in the possible solutions list, and also looks at how frequent a given word is in the english language. These strategies allow the bot to guess the word in about 3.8 guesses on average. Feel free to give it a try!

app.py: runs the wordle game and calls the recommend_words script. Also handles responses to the server.
    - This file is responsible for running the flask app
    - This file is responsible for selecting a word to be the solution via generate_solution
    - This file keeps track of words that could potentially be the solution by calling rw.remove_words() and storing the result in valid_guesses
    - This file compares a user's guess with the solution to return a list of colors to the server
    - This file also contains a testing script to evaluate the performance of the bot

recommend_words.py: contains the logic for recommending words.
    - This file determines which words from valid_guesses can be the solution, given known letter positions and colors (letter_indices) via remove_words()
        - letter_indices stores greens as positive indices and yellows as negative indices
    - This file recommends words to the user via recommend_words
        - This counts the letters in valid_guesses and scores words based on how many of these letters a guess contains, multiplied by the letter's frequency and the word frequency in word_frequencies

static/keypress.js: originally just handled key input, but now handles all logic on the client's side.
    - This file changes the website's html to display returned colors and inputted letters
    - This file communicates with the server by sending a guess and recieving a list of colors via POST