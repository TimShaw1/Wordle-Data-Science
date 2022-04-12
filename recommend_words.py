# Accepts the valid guesses list, a list of all vaid letters, a list of all invalid letters, and all known indices of the letters
def remove_words(guesses, invalid_letters, valid_letters, letter_indices):
    # Create a temporary list to store valid guesses
    temp = []
    temp_word = ""
    for word in guesses:
        temp.append(word)

    #loop through all words in temp and remove them if they contain invalid letters
    for word in temp:
        for letter in invalid_letters:
            if letter in word.upper():
                guesses.remove(word)
                break
    
    temp.clear()
    for word in guesses:
        temp.append(word)
    
    #loop through all words in temp and remove them if they do not contain valid letters
    for word in temp:
        if (len(valid_letters) > 0):
            for letter in valid_letters:
                if letter not in word.upper():
                    guesses.remove(word)
                    break

    temp.clear()
    for word in guesses:
        temp.append(word)

    green_indices = {}
    for letter in letter_indices:
        for i in range(len(letter_indices[letter])):
            if letter_indices[letter][i] > 0:
                if letter not in green_indices:
                    green_indices[letter] = [letter_indices[letter][i]]
                else:
                    green_indices[letter].append(letter_indices[letter][i])

    # Green letter in wrong place -- This does not completely work, but it solves the problem 
    # A more optimal solution is possible
    for word in temp:
        for i in range(5):
            if word[i].upper() in green_indices:
                temp_word = word
            # If green letter in right place, keep word
            # This makes an error since it keeps the word when seeing the first correct letter
            if word[i].upper() in green_indices and i in green_indices[word[i].upper()]:
                temp_word = ""
                break
                
        if temp_word in guesses and temp_word != "":
            if word == "bunny":
                print("bunny")
            guesses.remove(temp_word)
    
    temp.clear()
    for word in guesses:
        temp.append(word)


    # remove words that have a letter in the wrong place
    for word in temp:
        for i in range(5):
            # Yellow letter in wrong place
            if word[i].upper() in letter_indices and -(i+1) in letter_indices[word[i].upper()]:
                guesses.remove(word)
                break
    print(guesses)

# Determine frequency of letters in all possible solutions and reccomend words based on this
def recommend_words(guesses, valid_letters, invalid_letters, g):
    letter_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    # Count how many times each letter occurs in all possible words
    for guess in guesses:
        for i in range(5):
            letter_counts[guess[i].upper()] += 1
    
    # sort list of letters by count
    sorted_letters = sorted(letter_counts, key=letter_counts.get, reverse=False)

    seen_letters = []
    for letter in valid_letters:
        seen_letters.append(letter.upper())
    for letter in invalid_letters:
        seen_letters.append(letter.upper())

    for letter in seen_letters:
        sorted_letters.remove(letter)

    print(sorted_letters)

    # List to store top 10 words
    top_10 = []

    # Loop through each word in guess list and score it based on how many times each letter occurs
    for word in g:
        score = 0
        for i in range(len(sorted_letters)):
            if sorted_letters[i] in word.upper():
                score += i
        # if this score is higher than the lowest score in top_10, add it to top_10
        if len(top_10) < 10:
            top_10.append((word, score))
        else:
            if score > top_10[9][1]:
                top_10.append((word, score))
                top_10.sort(key=lambda x: x[1], reverse=True)
                top_10.pop()
    print(top_10)

    
    return top_10
            

            



    
