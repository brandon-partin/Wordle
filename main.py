import random
import rich
from rich.console import Console
from rich.prompt import Prompt
import re

import constants


SQUARES = {
        'correct_place': '🟩',
        'correct_letter': '🟨',
        'incorrect_letter': '⬛'
    }

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def load_5_letter_words():
    with open('five_letter_words.txt') as word_file:
        valid_5words = list(word_file.read().split())

    return valid_5words

def correct_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'

def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'

def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += correct_place(letter)
            wordle_pattern.append(SQUARES['correct_place'])
        elif letter in answer:
            guessed += correct_letter(letter)
            wordle_pattern.append(SQUARES['correct_letter'])
        else:
            guessed += incorrect_letter(letter)
            wordle_pattern.append(SQUARES['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern)

def game(console, chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []
    chosen_word = chosen_word.upper()
    while not end_of_game:
        guess = Prompt.ask(GUESS_STATEMENT).upper()
        #regex = []
        regex = re.findall("[a-zA-Z]", guess)
        while len(guess) != 5 or guess in already_guessed or len(regex) != 5:
            console.print(regex)
            console.print(len(regex))
            if guess in already_guessed:
                console.print("[red]You've already guessed this word!!\n[/]")
            elif len(regex) != 5:
                console.print("[red]Letters only, friend!!\n[/]")
            else:
                console.print('[red]Please enter a 5-letter word!!\n[/]')
            guess = Prompt.ask(GUESS_STATEMENT).upper()
            regex = re.findall("[a-zA-Z]", guess)
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        console.print(*all_words_guessed, sep="\n")
        if guess == chosen_word or len(already_guessed) == constants.TOTAL_GUESSES:
            end_of_game = True
    if len(already_guessed) == constants.TOTAL_GUESSES and guess != chosen_word:
        console.print(f"\n[red]WORDLE X/{constants.TOTAL_GUESSES}[/]")
        console.print(f'\n[green]Correct Word: {chosen_word}[/]')
    else:
        console.print(f"\n[green]WORDLE {len(already_guessed)}/{constants.TOTAL_GUESSES}[/]\n")
    console.print(*full_wordle_pattern, sep="\n")

WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE [/]\n'

if __name__=='__main__':
    console = Console()
    PLAYER_INSTRUCTIONS = "You may start guessing\n"
    words = load_5_letter_words()
    console.print("poops" in words)
    count = 0
    console.print(WELCOME_MESSAGE)
    GUESS_STATEMENT = "\nEnter your guess"

    for x in words:
        count += 1
    print(count)
    correctWord = random.choice(words)
    print(correctWord)
    print(correctWord[0])
    console.print(PLAYER_INSTRUCTIONS)
    game(console, correctWord)




#print(str(len(five_words)) + " from len()\n")
#count = 0
#for x in five_words:
#    count += 1
#print(str(count) + " from count\n")
#count = 0
#with open('five_letter_words.txt') as fp:
#    Lines = fp.readlines()
#    for line in Lines:
#        count += 1
#print(str(count) + " from file")
#fp.close()





#english_words = load_words()
#print(len(english_words))
    # demo print
  #  print('farts' in english_words)
#five_letter_words = open("five_letter_words.txt", "w")

#for x in english_words:
    #   print(x)
    #if len(x) == 5:
    #   print(x + "\n")
    #five_letter_words.write(x + "\n")

#five_letter_words.close()




