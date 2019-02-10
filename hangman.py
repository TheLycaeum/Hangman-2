# hangman.py

import random



def get_secret_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        good_words = []
        for i in f:
            i = i.strip()
            if len(i) <= 6:     # No short words
                continue
            if not i.isalpha(): # No punctuation
                continue
            if i[0].isupper():  # No proper nouns
                continue
            good_words.append(i)
    return random.choice(good_words)

def mask_line(word):
    return "*"*len(word)

def tries_left(tri):
    return 10 - tri

def guess_letter(word,letter,mask_line):
    if letter in word:
        x = 0
        for i in word:
            if i == letter:
                mask_line = mask_line[0:x] + letter + mask_line[x+1:]
            x = x + 1
        return mask_line
    else:
        return False

game = True
word = get_secret_word()
#print(word)
mask = mask_line(word)
x = 1
max_guess = 10
guesses = []
while game:
    print(mask)
    print(f"No: of guesses left {tries_left(x)}\n\n")
    letter = input("Your guess : ").lower()
    if letter in guesses:
        print("already guessed : {guesses} ")
        continue
    guess = guess_letter(word,letter,mask)
    if guess == False:
        print(mask)
        print("Wrong guess")
        guesses.append(letter)
        x = x + 1
    else:
        mask = guess
        print(mask)
    if mask == word:
        game = False
        print(f"Congrats, you won !!! word was {word}")
    else:
        print(f"guesses: {sorted(guesses)}\n\n")
        if x >= 10:
            print(f"Sorry, 10 guesses over, the word was : {word}")
            game = False






