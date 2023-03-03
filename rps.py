# File created by: Jaime Cesar Zorrilla
# Goal: Create a visually interactive game of RPS while allowing for the player's relative freedom.
# import libraries
 
from time import sleep
# Used to make the computer select a random choice for Rock, Paper, Scissors
from random import randint
# Comprehensive game library for use in python
import pygame as pg
# Allows use of directories
import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 1300
HEIGHT = 800
FPS = 30

# define colors. Used RGB (Red, Green, Blue)
# Tuples are immutable, so these set values are permanent
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initiallizes (turns on) pygame
# Specifically screen
pg.init()
# Specifically sound
pg.mixer.init()

# Opens a tab with these dimentions
screen = pg.display.set_mode((WIDTH, HEIGHT))
# Aforementioned tab is titled with the string value
pg.display.set_caption("Rock, Paper, Scissors")
# Provides time for FPS to work
clock = pg.time.Clock()
# Turns a visual saved in my folder into a variable to be used in the code
rock_image = pg.image.load(os.path.join(game_folder, "rock.jpg")).convert()
paper_image = pg.image.load(os.path.join(game_folder, "paper.jpg")).convert()
scissors_image = pg.image.load(os.path.join(game_folder, "scissors.jpg")).convert()
winner_image = pg.image.load(os.path.join(game_folder, "winner.jpg")).convert()
rockai_image = pg.image.load(os.path.join(game_folder, "rockai.jpg")).convert()
paperai_image = pg.image.load(os.path.join(game_folder, "paperai.jpg")).convert()
scissorsai_image = pg.image.load(os.path.join(game_folder, "scissorsai.jpg")).convert()
winner_image = pg.image.load(os.path.join(game_folder, "winner.jpg")).convert()
loser_image = pg.image.load(os.path.join(game_folder, "loser.jpg")).convert()
secretEnding_image = pg.image.load(os.path.join(game_folder, "secretEnding.jpg")).convert()
intro_image = pg.image.load(os.path.join(game_folder, "intro.jpg")).convert()
# Creates a rectangle for the image to be placed upon (saves location of each pixel of the image)
rock_image_rect = rock_image.get_rect()
paper_image_rect = paper_image.get_rect()
scissors_image_rect = scissors_image.get_rect()
rockai_image_rect = rockai_image.get_rect()
paperai_image_rect = paperai_image.get_rect()
scissorsai_image_rect = scissorsai_image.get_rect()
winner_image_rect = winner_image.get_rect()
loser_image_rect = loser_image.get_rect()
secretEnding_image_rect = secretEnding_image.get_rect()
intro_image_rect = intro_image.get_rect()

# Creates the cpu's choices
aiChoices = ['rock', 'paper', 'scissors']

# This function, at its end, prints one of the items of the 'choices' list as the computer's choice
def cpuRandomChoice():
    return aiChoices[randint(0,2)]

screen.fill(BLACK)
# Draw the former on the space provided by the latter.
screen.blit(intro_image, intro_image_rect)
pg.display.flip()
# Prints setup and into to game
print("Welcome to Rock, Paper, Scissors!")
print("Here you play and the computer in a game of rock, paper, scissors.")
print("If you wanted to play a person, just play normally. ¯\_(ツ)_/¯")
print("Without futher adieu...")
sleep(10)
print("let's play!")
print("Choose your hand, and I'll choose mine.")

# Creates the variables that determine which section of the code plays, allowing tie loops.
choosing = True
comparing = False
# As stated above, the funtion is all tied together so that it may loop as nessesary.
while comparing == True or choosing == True:
    # While true, the following happens
    while choosing:
        # Update game once per value of FPS (30) per second
        clock.tick(FPS)

        ###################### draw ########################
        # make the background black
        screen.fill(BLACK)
        # Draw the former on the space provided by the latter.
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, rock_image_rect)

        pg.display.flip()
        ################## player interact ####################
        # Every time the user intereacts with the computer
        for event in pg.event.get():
            # When one hits the x button at the top of the tab...
            if event.type == pg.QUIT:
                # ...the variable becomes false, causing the program to shut down.
                choosing = False
            ###################### get user input #########################
            #HCI - human computer interaction
            # mouse, controller, touchscreen, vr headset, ect.
            # This section allows the player to make their choice
            # When one clicks their mouse on the screen...
            if event.type == pg.MOUSEBUTTONUP:
                # print(pg.mouse.get_pos())
                # ...the x-value...
                # print(pg.mouse.get_pos()[0])
                # # ...and the y-value of the mouse's position is printed.
                # print(pg.mouse.get_pos()[1])
                # The coordinates of the mouse clicks are saved as varibles for later usage.
                global x
                global y
                global user
                x = pg.mouse.get_pos()[0]
                y = pg.mouse.get_pos()[1]
                mouse_coords = pg.mouse.get_pos()
                # if x < 474 and y < 355:
                #if x < my_image_rect.width + 1 and y < my_image_rect.height + 1:
                # If the coordinates of the mouse click are within with rock's picture...
                if rock_image_rect.collidepoint(mouse_coords) == True:
                    # ...print the following string.
                    print("You've chosen rock!")
                    user = "rock"
                    comparing = True
                    choosing = False
                # If the coordinates of the mouse click are within with paper's picture...
                elif paper_image_rect.collidepoint(mouse_coords) == True:
                    # ...print the following string.
                    print("You've chosen paper!")
                    user = "paper"
                    comparing = True
                    choosing = False
                # If the coordinates of the mouse click are within with scissors' picture...
                elif scissors_image_rect.collidepoint(mouse_coords) == True:
                    # ...print the following string.
                    print("You've chosen scissors!")
                    user = "scissors"
                    comparing = True
                    choosing = False
                # If not...
                else:
                    # ...print this string.
                    print("OH NO! You've chosen the abyss!")
                    sleep(3)
                    # make the background black
                    screen.fill(BLACK)
                    pg.display.flip()
                    sleep(2)
                    # Sets location of image
                    secretEnding_image_rect.x = 500
                    # Draw the former on the space provided by the latter.
                    screen.blit(secretEnding_image, secretEnding_image_rect)
                    pg.display.flip()
                    print("The world has fallen to eternal darkness...")
                    print("...as evil night blankets the landscape...")
                    print("...the Reaper comes for us all!")
                    print("GAME OVER")
                    print("GAME RESULT: TIE")
                    print("SECRET ENDING: DEATH TO ALL")
                    sleep(10)
                    pg.quit()

    
        ###################### update ########################
        # This section causes movement on screen
        # Causes the pixels of the images to move positively on the x-axis
        # if rock_image_rect.x < 100:
        #     rock_image_rect.x += 10
        # if paper_image_rect.x < 600:
        #     paper_image_rect.x += 10
        # if scissors_image_rect.x < 800:
        #     scissors_image_rect.x += 10    

    # Now the above function is a variable, allowing easier access.
    cpu = cpuRandomChoice()
    ####################### game ##########################
    # This section is the meat of the code, 
    while comparing:
        print("I have chosen...")
        cpu = cpuRandomChoice()
        cpu = "paper"
        if user == "rock":
            # make the background black
            screen.fill(BLACK)
            # Draw the former on the space provided by the latter.
            screen.blit(rock_image, rock_image_rect)
            pg.display.flip()
            if rock_image_rect.x < 499:
                rock_image_rect.x += 5
            sleep(3)
            print("ROCK!")
            sleep(3)
            print("PAPER!")
            sleep(3)
            print("SCISSORS!")
            sleep(3)
            print("SHOOT!")
            if cpu == "rock":
                screen.blit(rockai_image, rockai_image_rect)
                pg.display.flip()
                rockai_image_rect.x = 500
                rockai_image_rect.y = 400
                sleep(3)
                print("Welp! That's a tie.")
                sleep(5)
                print("Let's try again.")
                print("When the options return, choose again.")
                sleep(7)
                choosing = True
                comparing = False
            elif cpu == "paper":
                screen.blit(paperai_image, paperai_image_rect)
                pg.display.flip()
                paperai_image_rect.x = 600
                paperai_image_rect.y = 400
                sleep(3)
                print("HA! YOU FOOL!")
                sleep(2)
                print("Little did you know that I, LORD PAPER, was behind this game.")
                sleep(2)
                print("You have allowed me victory...")
                sleep(2)
                print("HENCE I DOOM YOUR WORLD TO DEATH BY PAPERCUT!")
                sleep(2)
                print("'Tis naught but a glorified rock, after all.")
                screen.fill(BLACK)
                screen.blit(loser_image, loser_image_rect)
                loser_image_rect.x = 500
                loser_image_rect.y = 200
                pg.display.flip()
                print("GAME OVER")
                print("GAME RESULT: LOSE")
                print("BAD ENDING 1: DEATH BY PAPERCUT")
                sleep(10)
                comparing = False
            else:
                print("Sucker!")
                comparing = False
        elif user == "paper":
            # make the background black
            screen.fill(BLACK)
            # Draw the former on the space provided by the latter.
            screen.blit(paper_image, paper_image_rect)
            pg.display.flip()
        elif user == "scissors":
            # make the background black
            screen.fill(BLACK)
            # Draw the former on the space provided by the latter.
            screen.blit(scissors_image, scissors_image_rect)
            pg.display.flip()

pg.quit()





" This game is most fun while reading                                                        "