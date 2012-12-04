# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
number = 0
guesses = 0

# define event handlers for control panel

def reset():
    rand_game = random.randrange(0,2)
    print ""
    print "NEW GAME!"
    if rand_game == 0:
        range100()
    else:
        range1000()
    print ""
    
    
def range100():
    # button that changes range to range [0,100) and restarts
    global number, guesses
    number = random.randrange(0,100)
    guesses = 7
    print "The range is 0 - 100"
    print "The number of guesses remaining: ", guesses
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global number, guesses
    number = random.randrange(0,1000)
    guesses = 10
    print "The range is 0 - 1000"
    print "The number of guesses remaining: ", guesses
    
    
    
def get_input(guess):
    global number, guesses
    my_guess = int(guess)
    guesses -= 1
    print "Guess was ", my_guess
    print "Number of guesses remaining: ", guesses
    if guesses < 0:
        print "You lose! The number was ", number
        reset()
    elif number < my_guess:
        print "Guess lower!"
    elif number > my_guess:
        print "Guess higher!"
    else: #number == my_guess:
        print "You guessed it! The number is ", number
        reset()
    print ""

    
# create frame

frame = simplegui.create_frame("Guess the Number!", 300, 300)


# register event handlers for control elements

frame.add_button("Range is [0-100]", range100, 150)
frame.add_button("Range is [0-1000]", range1000, 150)
frame.add_input("Guess the number", get_input, 100)

# start frame
frame.start()
reset()

# always remember to check your completed program against the grading rubric
