import pygame as pg
import time
from tkinter.simpledialog import askstring
from tkinter import simpledialog
import tkinter
root = tkinter.Tk()
root.withdraw()
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
pg.mixer.init()

word = askstring("Enter a word", "Enter a word", show='*')
word = lower(word)
word_check = "" #used to check if words are equal by adding spaces between the letters in word
running = True
num_wrong = 0

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Hangman!")
clock = pg.time.Clock()

def create_surface(input_word):
    screen.fill(BLACK)
    textsurface = myfont.render(input_word, True, (WHITE))
    screen.blit(textsurface,(0,0))
    noose_num = "Hang" + str(num_wrong) + ".png"
    noose = pg.image.load("images/" + noose_num)
    noose = pg.transform.scale(noose, (400, 400))
    screen.blit(noose, (100, 200)) 
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
    screen.fill(BLACK)
    pg.font.init()
    myfont = pg.font.SysFont('Arial', 45)
    create_surface(hidden_word)
    pg.display.flip()
    correct_guess = False
    while hidden_word != word:
        jeopardy = open("hangman-audio/Jeopardy.mp3")
        pg.mixer.music.load(jeopardy)
        pg.mixer.music.play(-1)
        num_attempt = myfont.render("Attempts left: " + str(7-num_wrong), True, (WHITE))
        screen.blit(num_attempt,(250,HEIGHT-50))
        pg.display.update()
        guess = askstring("Guess a letter", "Guess a letter")
        hidden_word_list = list(hidden_word)
        for index,char in enumerate(word):
            if char == guess:
                hidden_word_list[index * 2] = guess
                hidden_word = ""
                correct_guess = True
                for i in hidden_word_list:
                    hidden_word += i
        if lower(guess) == word:
            create_surface(hidden_word)
            pg.mixer.music.load("hangman-audio/Victory.mp3")
            pg.mixer.music.play()
            textsurface = myfont.render("You Won!", True, (WHITE))
            screen.blit(textsurface,(175, 600))
            pg.display.update()
            time.sleep(5)
            running = False
            break
        if correct_guess == True:
            pg.mixer.music.stop()
            jeopardy.close()
            pg.mixer.music.load("hangman-audio/Correct.mp3")
            pg.mixer.music.play()
            time.sleep(1.5)
        if hidden_word == word_check:
            create_surface(hidden_word)
            pg.mixer.music.load("hangman-audio/Victory.mp3")
            pg.mixer.music.play()
            textsurface = myfont.render("You Won!", True, (WHITE))
            screen.blit(textsurface,(175, 600))
            pg.display.update()
            time.sleep(5)
            running = False
            break
        else:
            if correct_guess == False:
                num_wrong += 1
                pg.mixer.music.stop()
                jeopardy.close()
                pg.mixer.music.load("hangman-audio/Wrong_Buzzer.mp3")
                pg.mixer.music.play()
                time.sleep(2)
            correct_guess = False
            create_surface(hidden_word)
            num_attempt = myfont.render("Attempts left: " + str(7-num_wrong), True, (WHITE))
            screen.blit(num_attempt,(250,HEIGHT-50))
            pg.display.update()
            if num_wrong == 7:
                screen.fill(BLACK)
                textsurface = myfont.render("You lose!", True, (WHITE))
                screen.blit(textsurface,(200, 100))
                textsurface = myfont.render("The word is " + word, True, (WHITE))
                screen.blit(textsurface,(150, 600))
                noose = pg.image.load("images/Hang7.png")
                noose = pg.transform.scale(noose, (400, 400))
                screen.blit(noose, (100, 200)) 
                pg.display.update()
                running = False
                time.sleep(3)
                break
pg.display.quit()
pg.quit()
quit()
root.mainloop()            
