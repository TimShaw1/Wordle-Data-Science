# Accepts the valid guesses list and a letter known to be in the word
# Returns an array of all words that contain the letter
def remove_words(guesses, invalid_letters, valid_letters, letter_indices):
    # Create a temporary list to store valid guesses
    temp = []
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
        for letter in valid_letters:
            if letter not in word.upper():
                guesses.remove(word)
                break

    temp.clear()
    for word in guesses:
        temp.append(word)

    # remove words that have a green letter in the wrong place
    for word in temp:
        for i in range(5):
            # Yellow letter in wrong place
            if word[i].upper() in letter_indices and letter_indices[word[i].upper()] == -i:
                guesses.remove(word)
                break
            # Green letter in wrong place
            #TODO: Fix duplicate letter cases
            if word[i].upper() in letter_indices and letter_indices[word[i].upper()] != i and letter_indices[word[i].upper()] > 0:
                guesses.remove(word)
                break



    
