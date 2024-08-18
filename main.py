'''
Author: Scott Field
Date: 8/17/2024
Version: 1.0
Purpose:
Create a Simon Says game using Python with the following features:
- A start screen that allows the user to:
    1: Begin Game
    2: Set Game To Either Close If the User Loses a Round or to Continue Until Exit button (game screen) pressed
- A game screen that allows the user to:
    1: Play Simon Says
        - Outputs whether user choices are correct using text
        - Visually Counts down the time the user has to make choices (DONE)
        - Logs number of 
        - Exits if user makes an incorrect choice
        - Exits if user selects an exit button
'''

import pygame
import random
import time
# By importing Button we can access methods from the Button class
from button import Button
from timer import Label
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
GREEN_ON = (0, 255, 0)
GREEN_OFF = (0, 227, 0)
RED_ON = (255, 0, 0)
RED_OFF = (227, 0, 0)
BLUE_ON = (0, 0, 255)
BLUE_OFF = (0, 0, 227)
YELLOW_ON = (255, 255, 0)
YELLOW_OFF = (227, 227, 0)

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Pass in respective sounds for each color
GREEN_SOUND = pygame.mixer.Sound("sounds/bell1.mp3") # bell1
RED_SOUND = pygame.mixer.Sound("sounds/bell2.mp3") # bell2
BLUE_SOUND = pygame.mixer.Sound("sounds/bell3.mp3") # bell3
YELLOW_SOUND = pygame.mixer.Sound("sounds/bell4.mp3") # bell4

# Button Sprite Objects
green = Button(GREEN_ON, GREEN_OFF, GREEN_SOUND, 40, 400)
red = Button(RED_ON, RED_OFF, RED_SOUND, 280, 400)
blue = Button(BLUE_ON, BLUE_OFF, BLUE_SOUND, 520, 400)
yellow = Button(YELLOW_ON, YELLOW_OFF, YELLOW_SOUND, 760, 400)

#Timer Label
timer_label = Label(position = (485,350), size = 72)

# Variables
colors = ["green", "red", "blue", "yellow"]
cpu_sequence = []
players_sequence = []
choice = ""

'''
Draws game board
'''
def draw_board():
    # Call the draw method on all four button objects
    green.draw(SCREEN)
    red.draw(SCREEN)
    blue.draw(SCREEN)
    yellow.draw(SCREEN)

'''
Chooses a random color and appends to cpu_sequence.
Illuminates randomly chosen color.
'''
def cpu_turn():
    # pick random color
    choice = random.choice(colors)
    # update cpu sequence
    cpu_sequence.append(choice)
    # match statement to update screen
    match choice:
        case "green":
            green.update(SCREEN)
        case "red":
            red.update(SCREEN)
        case "blue":
            blue.update(SCREEN)
        case "yellow":
            yellow.update(SCREEN)

'''
Plays pattern sequence that is being tracked by cpu_sequence
'''
def repeat_cpu_sequence():
    if(len(cpu_sequence) != 0):
        for color in cpu_sequence:
            #if elif else to update screen
            if color == "green":
                green.update(SCREEN)
            elif color == "red":
                red.update(SCREEN)
            elif color == "blue":
                blue.update(SCREEN)
            else:
                yellow.update(SCREEN)
            pygame.time.wait(500)

'''
After cpu sequence is repeated the player must attempt to copy the same
pattern sequence.
The player is given 3 seconds to select a color and checks if the selected
color matches the cpu pattern sequence.
If player is unable to select a color within 3 seconds then the game is
over and the pygame window closes.
'''
def player_turn():
    turn_time = time.time()
    players_sequence = []

    while time.time() <= turn_time + 3 and len(players_sequence) < len(cpu_sequence):
        #Keep  track of remaining time
        time_left = turn_time + 3 - time.time()
        #Output Remaining Time To Screen
        timer_label.update_time(SCREEN, round(time_left))
        pygame.display.update()

        for event in pygame.event.get():
            # button click occured
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # Grab the current position of mouse here
                pos = pygame.mouse.get_pos()
                
                #Detect which button was selected
                if green.selected(pos):  
                    green.update(SCREEN)  
                    players_sequence.append("green")  
                elif red.selected(pos):
                    red.update(SCREEN)
                    players_sequence.append("red")
                elif blue.selected(pos):
                    blue.update(SCREEN)
                    players_sequence.append("blue")
                elif yellow.selected(pos):
                    yellow.update(SCREEN)
                    players_sequence.append("yellow")

                #If any of the buttons were pressed
                if players_sequence:
                    # check if player choice was correct
                    check_sequence(players_sequence)
                    # reset timer
                    turn_time = time.time()
                
                
                
# If player does not select a button within 3 seconds then the game closes
    if not time.time() <= turn_time + 3:
        game_over()

'''
Checks if player's move matches the cpu pattern sequence
'''
def check_sequence(players_sequence):
    if players_sequence != cpu_sequence[:len(players_sequence)]:
        game_over()
    else:
        timer_label.clear(SCREEN)


'''
Quits game and closes pygame window
'''
def game_over():
    pygame.quit()
    quit()

'''
Executes game loop if script is selected as main
'''
if __name__ == "__main__":
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                game_over() 
        
        pygame.display.update()

        # draws buttons onto pygame screen
        draw_board() 
        # repeats cpu sequence if it's not empty
        repeat_cpu_sequence() 
        # cpu randomly chooses a new color
        cpu_turn() 
        # player tries to recreate cpu sequence
        player_turn() 
        # waits one second before repeating cpu sequence
        pygame.time.wait(1000) 
        CLOCK.tick(60)