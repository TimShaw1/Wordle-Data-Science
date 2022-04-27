# Accepts the valid guesses list, a list of all vaid letters, a list of all invalid letters, and all known indices of the letters
def remove_words(guesses, invalid_letters, valid_letters, letter_indices, word_frequencies):
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
        if (len(valid_letters) > 0):
            for letter in valid_letters:
                if letter not in word.upper():
                    guesses.remove(word)
                    break

    temp.clear()
    for word in guesses:
        temp.append(word)

    # Used to track if we should skip to next word in loop
    skip = False
    # Green letter in wrong place 
    for word in temp:
        skip = False
        for letter in letter_indices:
            for index in letter_indices[letter]:
                if not skip and index >= 0:
                    if letter in word.upper():
                        if word[index].upper() != letter:
                            guesses.remove(word)
                            skip = True
                            break

    
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

    # Sort guesses by english word frequency
    freq_sort = []
    for item in guesses:
        if item in word_frequencies:
            if not float(word_frequencies[item]) < 1.000013:
                freq_sort.append([item, word_frequencies[item]])
    freq_sort.sort(key=lambda x: x[1], reverse=True)

    guesses.clear()

    for list in freq_sort:
        guesses.append(list[0])




# Determine frequency of letters in all possible solutions and reccomend words based on this
def recommend_words(guesses, valid_letters, invalid_letters, g, word_frequencies):
    letter_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    # Count how many times each letter occurs in all possible words
    for guess in guesses:
        for i in range(5):
            letter_counts[guess[i].upper()] += 1
            if guess in word_frequencies:
                letter_counts[guess[i].upper()] *= float(word_frequencies[guess])
    
    # sort list of letters by count
    sorted_letters = sorted(letter_counts, key=letter_counts.get, reverse=False)

    seen_letters = []
    for letter in valid_letters:
        seen_letters.append(letter.upper())
    for letter in invalid_letters:
        seen_letters.append(letter.upper())

    for letter in seen_letters:
        sorted_letters.remove(letter)


    # List to store top 10 words
    top_10 = []

    # Loop through each word in guess list and score it based on how many times each letter occurs
    for word in g:
        score = 0
        for i in range(len(sorted_letters)):
            if sorted_letters[i] in word.upper():
                score += i
        if word in word_frequencies:
            score += float(word_frequencies[word]) * 2
        # if this score is higher than the lowest score in top_10, add it to top_10
        if len(top_10) < 10:
            top_10.append((word, score))
        else:
            if score > top_10[9][1]:
                top_10.append((word, score))
                top_10.sort(key=lambda x: x[1], reverse=True)
                top_10.pop()

    
    # Remove score list element from top_10
    final_top_10 = []
    for i in range(len(top_10)):
        final_top_10.append(top_10[i][0])
    
    return final_top_10
            