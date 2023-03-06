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
HEIGHT = 700
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
pg.display.set_caption("Rock, Paper, Scissors Epic Duel")
# Provides time for FPS to work
clock = pg.time.Clock()
# Turns a visual saved in my folder into a variable to be used in the code
rock_image = pg.image.load(os.path.join(game_folder, "rock.jpg")).convert()
paper_image = pg.image.load(os.path.join(game_folder, "paper.jpg")).convert()
scissors_image = pg.image.load(os.path.join(game_folder, "scissors.jpg")).convert()
rock2_image = pg.image.load(os.path.join(game_folder, "rock2.jpg")).convert()
paper2_image = pg.image.load(os.path.join(game_folder, "paper2.jpg")).convert()
scissors2_image = pg.image.load(os.path.join(game_folder, "scissors2.jpg")).convert()
winner_image = pg.image.load(os.path.join(game_folder, "winner.jpg")).convert()
rockai_image = pg.image.load(os.path.join(game_folder, "rockai.jpg")).convert()
paperai_image = pg.image.load(os.path.join(game_folder, "paperai.jpg")).convert()
scissorsai_image = pg.image.load(os.path.join(game_folder, "scissorsai.jpg")).convert()
winner_image = pg.image.load(os.path.join(game_folder, "winner.jpg")).convert()
loser_image = pg.image.load(os.path.join(game_folder, "loser.jpg")).convert()
secretEnding_image = pg.image.load(os.path.join(game_folder, "secretEnding.jpg")).convert()
intro_image = pg.image.load(os.path.join(game_folder, "intro.jpg")).convert()
me_image = pg.image.load(os.path.join(game_folder, "me.jpg")).convert()
you_image = pg.image.load(os.path.join(game_folder, "you.jpg")).convert()
# Creates a rectangle for the image to be placed upon (saves location of each pixel of the image)
rock_image_rect = rock_image.get_rect()
paper_image_rect = paper_image.get_rect()
scissors_image_rect = scissors_image.get_rect()
rock2_image_rect = rock2_image.get_rect()
paper2_image_rect = paper2_image.get_rect()
scissors2_image_rect = scissors2_image.get_rect()
rockai_image_rect = rockai_image.get_rect()
paperai_image_rect = paperai_image.get_rect()
scissorsai_image_rect = scissorsai_image.get_rect()
winner_image_rect = winner_image.get_rect()
loser_image_rect = loser_image.get_rect()
secretEnding_image_rect = secretEnding_image.get_rect()
intro_image_rect = intro_image.get_rect()
you_image_rect = you_image.get_rect()
me_image_rect = me_image.get_rect()

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
sleep(2)
print("Here you play and the computer in a game of rock, paper, scissors.")
sleep(2)
print("If you wanted to play against a person, just play normally. ¯\_(ツ)_/¯")
sleep(2)
print("Without futher adieu...")
sleep(2)
print("let's play!")
sleep(2)
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
        # Sets the locations of the images
        rock_image_rect.x = 100
        paper_image_rect.x = 600
        scissors_image_rect.x = 800
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
                    print("*You've chosen rock*")
                    user = "rock"
                    # Activates loop 2 and turns off loop 1
                    comparing = True
                    choosing = False
                # If the coordinates of the mouse click are within with paper's picture...
                elif paper_image_rect.collidepoint(mouse_coords) == True:
                    # ...print the following string.
                    print("*You've chosen paper*")
                    user = "paper"
                    # Activates loop 2 and turns off loop 1
                    comparing = True
                    choosing = False
                # If the coordinates of the mouse click are within with scissors' picture...
                elif scissors_image_rect.collidepoint(mouse_coords) == True:
                    # ...print the following string.
                    print("*You've chosen scissors*")
                    user = "scissors"
                    # Activates loop 2 and turns off loop 1
                    comparing = True
                    choosing = False
                # If none are clicked...
                else:
                    # ...print this string.
                    print("OH NO! You've chosen the abyss!")
                    sleep(3)
                    # make the background black
                    screen.fill(BLACK)
                    pg.display.flip()
                    sleep(2)
                    print("The world has fallen to eternal darkness...")
                    sleep(2)
                    print("...as evil night blankets the landscape...")
                    sleep(2)
                    print("...the Reaper comes for us all!")
                    # Sets location of image
                    secretEnding_image_rect.x = 500
                    # Draw the former on the space provided by the latter.
                    screen.blit(secretEnding_image, secretEnding_image_rect)
                    pg.display.flip()
                    sleep(2)
                    print("GAME OVER")
                    print("GAME RESULT: TIE")
                    print("SECRET ENDING: DEATH TO ALL")
                    sleep(5)
                    pg.quit()
          

    # Now the above function is a variable, allowing easier access.
    cpu = cpuRandomChoice()

    ####################### game ##########################
    # This section is the meat of the code, 
    while comparing:
        clock.tick(FPS)
        # make the background black
        screen.fill(BLACK)
        pg.display.flip()
        for event in pg.event.get():
            # When one hits the x button at the top of the tab...
            if event.type == pg.QUIT:
                # ...the variable becomes false, causing the program to shut down.
                comparing = False
        me_image_rect.x = 525
        me_image_rect.y = 550
        you_image_rect.x = 500
        screen.blit(me_image, me_image_rect)
        screen.blit(you_image, you_image_rect)
        pg.display.flip()
        # Update game once per value of FPS (30) per second
        print("I have chosen...")
        cpu = cpuRandomChoice()
        sleep(2)
        print("Ready?")
        sleep(2)
        rock2_image_rect.x = 450
        rock2_image_rect.y = 175
        screen.blit(rock2_image, rock2_image_rect)
        pg.display.flip()
        print("ROCK!")
        sleep(1)
        screen.fill(BLACK)
        me_image_rect.x = 525
        me_image_rect.y = 550
        you_image_rect.x = 500
        screen.blit(me_image, me_image_rect)
        screen.blit(you_image, you_image_rect)
        paper2_image_rect.x = 600
        paper2_image_rect.y = 250
        screen.blit(paper2_image, paper2_image_rect)
        pg.display.flip()
        print("PAPER!")
        sleep(1)
        screen.fill(BLACK)
        me_image_rect.x = 525
        me_image_rect.y = 550
        you_image_rect.x = 500
        screen.blit(me_image, me_image_rect)
        screen.blit(you_image, you_image_rect)
        scissors2_image_rect.x = 450
        scissors2_image_rect.y = 165
        screen.blit(scissors2_image, scissors2_image_rect)
        pg.display.flip()
        print("SCISSORS!")
        sleep(1)
        screen.fill(BLACK)
        me_image_rect.x = 525
        me_image_rect.y = 550
        you_image_rect.x = 500
        screen.blit(me_image, me_image_rect)
        screen.blit(you_image, you_image_rect)
        pg.display.flip()
        print("SHOOT!")
        sleep(0.5)
        if user == "rock":
            # Dispays player's rock
            screen.fill(BLACK)
            rock_image_rect.x = 450
            screen.blit(rock_image, rock_image_rect)
            pg.display.flip()
            if cpu == "rock":
                # Displays the AI's rock
                rockai_image_rect.x = 450
                rockai_image_rect.y = 350
                screen.blit(rockai_image, rockai_image_rect)
                pg.display.flip()
                sleep(1)
                print("Welp! That's a tie.")
                sleep(2)
                print("Let's try again.")
                sleep(2)
                print("When the options return, choose again.")
                sleep(3)
                # Activates loop 1 and turns off loop 2
                choosing = True
                comparing = False
            elif cpu == "paper":
                # Displays the AI's paper
                paperai_image_rect.x = 600
                paperai_image_rect.y = 500
                screen.blit(paperai_image, paperai_image_rect)
                pg.display.flip()
                sleep(1)
                print("HA! YOU FOOL!")
                sleep(2)
                print("Little did you know that I, LORD PAPER, was behind this game.")
                sleep(2)
                print("You have allowed me victory...")
                sleep(2)
                print("HENCE I DOOM YOUR WORLD TO DEATH BY PAPERCUT!")
                sleep(1.5)
                screen.fill(BLACK)
                pg.display.flip()
                print("'Tis naught but a glorified rock, after all.")
                sleep(2)
                screen.fill(BLACK)
                loser_image_rect.x = 450
                loser_image_rect.y = 100
                screen.blit(loser_image, loser_image_rect)
                pg.display.flip()
                print("GAME OVER")
                print("GAME RESULT: LOSE")
                print("BAD ENDING 1: DEATH BY PAPERCUT")
                sleep(3)
                # Turns off loop 2
                comparing = False
            else:
                # Displays the AI's scissors
                scissorsai_image_rect.x = 450
                scissorsai_image_rect.y = 300
                screen.blit(scissorsai_image, scissorsai_image_rect)
                pg.display.flip()
                sleep(1)
                print("NO! MY MIGHTY BLADES!")
                sleep(2)
                print("I HAVE FELLED MANY WITH MINE SCISSORS!")
                sleep(2)
                print("*sigh*")
                sleep(2)
                print("You were a worthy opponent.")
                sleep(2)
                print("Twas a fitting end for mine blade.")
                sleep(2)
                print("BUT!")
                sleep(2)
                print("Next we meet, I expect an even greater battle...")
                sleep(2)
                print("against your stone.")
                sleep(2)
                screen.fill(BLACK)
                winner_image_rect.x = 125
                winner_image_rect.y = -150
                screen.blit(winner_image, winner_image_rect)
                pg.display.flip()
                print("GAME OVER")
                print("GAME RESULT: WIN")
                print("GOOD ENDING 1: HONORABLE WARRIOR")
                sleep(3)
                # Turns off loop 2
                comparing = False
        elif user == "paper":
            screen.fill(BLACK)
            paper_image_rect.x = 600
            # Draw the former on the space provided by the latter.
            screen.blit(paper_image, paper_image_rect)
            pg.display.flip()
            if cpu == "rock":
                # Displays the AI's rock
                rockai_image_rect.x = 450
                rockai_image_rect.y = 350
                screen.blit(rockai_image, rockai_image_rect)
                pg.display.flip()
                sleep(1)
                print("*You covered the strange man and his rock with the paper he gave you*")
                sleep(2)
                print("*Underneath the paper you hear angry shouting*")
                sleep(2)
                print("*You can't understand, but you're pretty sure you don't want to*")
                sleep(2)
                print("*You take the opportunity to run away*")
                sleep(2)
                print("*You don't think you'll forget this strange encounter*")
                sleep(2)
                screen.fill(BLACK)
                winner_image_rect.x = 125
                winner_image_rect.y = -150
                screen.blit(winner_image, winner_image_rect)
                pg.display.flip()
                print("GAME OVER")
                print("GAME RESULT: WIN")
                print("GOOD ENDING 2: MUFFLED")
                sleep(3)
                # Turns off loop 2
                comparing = False
            elif cpu == "paper":
                # Displays the AI's paper
                paperai_image_rect.x = 600
                paperai_image_rect.y = 500
                screen.blit(paperai_image, paperai_image_rect)
                pg.display.flip()
                sleep(1)
                print("Welp! That's a tie.")
                sleep(2)
                print("Let's try again.")
                sleep(2)
                print("When the options return, choose again.")
                sleep(3)
                # Activates loop 1 and turns off loop 2
                choosing = True
                comparing = False
            else:
                # Displays the AI's scissors
                scissorsai_image_rect.x = 450
                scissorsai_image_rect.y = 300
                screen.blit(scissorsai_image, scissorsai_image_rect)
                pg.display.flip()
                sleep(1)
                print("...")
                sleep(2)
                print("what...")
                sleep(2)
                print("is that?")
                sleep(2)
                print("What ON EARTH did YOU think you could do with PAPER!")
                sleep(2)
                print("ATTACK!? DEFEND!?")
                sleep(2)
                print("Well, failed warrior, meet mine blade.")
                sleep(2)
                print("Perchance you could learn proper combat in death.")
                sleep(2)
                screen.fill(BLACK)
                loser_image_rect.x = 450
                loser_image_rect.y = 100
                screen.blit(loser_image, loser_image_rect)
                pg.display.flip()
                print("GAME OVER")
                print("GAME RESULT: LOSE")
                print("BAD ENDING 2: SLICED AND DICED")
                sleep(3)
                # Turns off loop 2
                comparing = False
        elif user == "scissors":
            screen.fill(BLACK)
            scissors_image_rect.x = 450
            # Draw the former on the space provided by the latter.
            screen.blit(scissors_image, scissors_image_rect)
            pg.display.flip()
            if cpu == "rock":
                # Displays the AI's rock
                rockai_image_rect.x = 450
                rockai_image_rect.y = 350
                screen.blit(rockai_image, rockai_image_rect)
                pg.display.flip()
                sleep(1)
                print("AIGHT! Let's see who wins!")
                sleep(2)
                print("Your metal, or my stone.")
                sleep(2)
                print("*Holding your scissors, you rush your opponent*")
                sleep(2)
                print("*You go in with a lunge...*")
                sleep(2)
                print("*...as he blo--*")
                sleep(2)
                print("*...*")
                sleep(2)
                print("*Oh. You tripped and landed face-first*")
                sleep(2)
                print("*On the scissors*")
                sleep(2)
                print("*Ow*")
                sleep(2)
                screen.fill(BLACK)
                loser_image_rect.x = 450
                loser_image_rect.y = 100
                screen.blit(loser_image, loser_image_rect)
                pg.display.flip()
                print("GAME OVER")
                print("GAME RESULT: LOSE")
                print("BAD ENDING 3: DON'T RUN WITH SCISSORS")
                sleep(3)
                # Turns off loop 2
                comparing = False
            elif cpu == "paper":
                # Displays the AI's paper
                paperai_image_rect.x = 600
                paperai_image_rect.y = 500
                screen.blit(paperai_image, paperai_image_rect)
                pg.display.flip()
                sleep(1)
                print("AH! MY DEFENCES!")
                sleep(2)
                print("NO! YOU WILL NOT STOP ME, PATHEIC PEASANT!")
                sleep(2)
                print("THE WORLD WILL FEAR ME, LORD PAPER!")
                sleep(2)
                print("YOU WILL BOW! YOU WILL OBE--")
                sleep(2)
                print("*You take his rambling as an opening...*")
                sleep(2)
                print("*...and silence him. Pemanantly*")
                sleep(2)
                print("*The world can now sleep in papercut-less peace*")
                sleep(2)
                print("*Good job!*")
                sleep(2)
                screen.fill(BLACK)
                winner_image_rect.x = 125
                winner_image_rect.y = -150
                screen.blit(winner_image, winner_image_rect)
                pg.display.flip()
                print("GAME OVER")
                print("GAME RESULT: WIN")
                print("GOOD ENDING 3: END OF THE DARK LORD")
                sleep(3)
                # Turns off loop 2
                comparing = False
            else:
                # Displays the AI's scissors
                scissorsai_image_rect.x = 450
                scissorsai_image_rect.y = 300
                screen.blit(scissorsai_image, scissorsai_image_rect)
                pg.display.flip()
                sleep(1)
                print("Welp! That's a tie.")
                sleep(2)
                print("Let's try again.")
                sleep(2)
                print("When the options return, choose again.")
                sleep(3)
                # Activates loop 1 and turns off loop 2
                choosing = True
                comparing = False

pg.quit()