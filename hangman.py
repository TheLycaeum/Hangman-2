# hangman.py
import random


def get_secret_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        good_words = []
        for i in f:
            i = i.strip()
            if len(i) <= 6:      # No short words
                continue
            if not i.isalpha():  # No punctuation
                continue
            if i[0].isupper():   # No proper nouns
                continue
            good_words.append(i)
    return random.choice(good_words)


def mask_line(word):
    return "*"*len(word)


def tries_left(tri):
    return 10 - tri


def guess_letter(word, letter, mask_line):
    if letter in word:
        x = 0
        for i in word:
            if i == letter:
                mask_line = mask_line[0:x] + letter + mask_line[x+1:]
            x = x + 1
        return mask_line
    else:
        return False


def play():
    game = True
    word = get_secret_word()
    mask = mask_line(word)
    x = 1
    guesses = []
    while game:
        print(mask, end="\n\n")
        print("Number of guesses left {}\n\n".format(tries_left(x)))
        letter = input("Your guess : ").lower()
        if letter in guesses:
            print("already guessed : {} ".format(guesses))
            continue
        guess = guess_letter(word, letter, mask)
        if guess == False:
            print("Wrong guess")
            guesses.append(letter)
            x = x + 1
        else:
            mask = guess
            print(mask)
        if mask == word:
            game = False
            print("Congrats, you won !!! word was {}".format(word))
        else:
            print("guesses: {sorted(guesses)}\n\n".format(guesses=guesses))
            if x >= 10:
                print("Sorry, 10 guesses over, the word was : {word}".format(word=word))
                game = False


def loop_play():
    print("""
          Hi this is Pavanan's hangman game !
          Rules:
          - You have 10 tries to guess the word.
          - Your word is hidden using "*"'s. number of stars is same as the
            number of letters in the word
          - Enter one letter as guess in each chance.
          - After each guess, a list of previous guesses will be shown in
            alphabetical order.
          - If you want to continue playing, press 'y' after the game !
            \n\n\n""")
    play()
    loop = True
    while loop:
        ans = input("\nDo you want to try again ?(y/n) ")
        if ans == "y":
            print("starting again \n\n")
            play()
        else:
            loop = False
            print("Exiting.")


loop_play()
