import getpass
import pygame as pg
import os
word = str(getpass.getpass("Enter your word: "))
word_check = "" #used to check if words are equal by adding spaces between the letters in word
for i in word:
    word_check += i
    word_check += " "
hidden_word = ""
for i in range(len(word)):
    hidden_word += "_"
    hidden_word += " "
os.system("/usr/bin/clear") #clears terminal
print(hidden_word)
while hidden_word != word:
    guess = input("Guess a letter: ")
    hidden_word_list = list(hidden_word)
    for index,char in enumerate(word):
        if char == guess:
            hidden_word_list[index * 2] = guess
            hidden_word = ""
            for i in hidden_word_list:
                hidden_word += i
    if hidden_word == word_check:
        print("The secret word is " + word)
        print("You Won!")
        break
    else:
        print(hidden_word)
            
