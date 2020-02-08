import getpass
import pygame as pg
import os
import time
from sys import exit

WIDTH = 500
HEIGHT = 700
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pg.init()
#pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Hangman!")
clock = pg.time.Clock()

word = str(getpass.getpass("Enter your word: "))
word_check = "" #used to check if words are equal by adding spaces between the letters in word
running = True
num_wrong = 0
def create_surface(input_word):
    screen.fill(BLACK)
    textsurface = myfont.render(input_word, True, (WHITE))
    screen.blit(textsurface,(0,0))
    noose_num = "Hang" + str(num_wrong) + ".png"
    noose = pg.image.load("images/" + noose_num)
    screen.blit(noose, (250, 350))
    pg.display.update()            
while running == True:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            quit()
            exit()
    for i in word:
        word_check += i
        word_check += " "
    hidden_word = ""
    for i in range(len(word)):
        hidden_word += "_"
        hidden_word += " "
    os.system("/usr/bin/clear") #clears terminal
    print(hidden_word)
    screen.fill(BLACK)
    pg.font.init()
    myfont = pg.font.SysFont('Arial', 45)
    create_surface(hidden_word)
    pg.display.flip()
    correct_guess = False
    while hidden_word != word:
        guess = input("Guess a letter: ")
        hidden_word_list = list(hidden_word)
        for index,char in enumerate(word):
            if char == guess:
                hidden_word_list[index * 2] = guess
                hidden_word = ""
                correct_guess = True
                for i in hidden_word_list:
                    hidden_word += i
        if hidden_word == word_check:
            print("The secret word is " + word)
            print("You Won!")
            create_surface(hidden_word)
            time.sleep(2)
            running = False
            break
        else:
            if correct_guess == False:
                num_wrong += 1
            correct_guess = False
            create_surface(hidden_word)
            print(hidden_word)
pg.display.quit()
pg.quit()
quit()
            
