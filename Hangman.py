import random

def choose_word():
    with open('sowpods.txt', 'r') as sow:
        word = ''.join(random.choices(sow.readlines()))
        return word

def display_word(word,guessed_letter):
    global disp_word
    if guessed_letter == ' ':
        disp_word = list('_' * (len(word)))
    for i in range(len(word)):
        if word[i] == guessed_letter:
            disp_word[i] = guessed_letter

    print(''.join(disp_word))

while True:
    print("Welcome to Hangman!")
    word = choose_word().rstrip()
    display_word(word,' ')
    print(word)
    count = 6
    while ''.join(disp_word)!= word and count > 0:
        guessed_letter = input("You have {} guesses left, Guess your letter: ".format(count) ).upper()
        count = count - 1
        display_word(word,guessed_letter)

    if ''.join(disp_word) == word:
        print("Congrats, you guessed it right!!")
    else:
        print("Sorry, your guesses has been exhausted")

    ask = ' '
    while ask != 'Y' and ask != 'N':
        ask = input("Would you like to play again? y/n").upper()
    if ask == 'N':
        break
