import simplegui
import random

WIDTH = 800
HEIGHT = 400

def init():
    global values, player_choice, computer_choice, result
    values = ['rock', 'Spock', 'paper', 'lizard', 'scissors']
    player_choice = ''
    computer_choice = ''
    result = ''

def number_to_name(number):
    return values[number]
    
def name_to_number(name): 
    i = 0
    for item in values:
        if item == name:
            return i
        i += 1

def rpsls(guess):
    global result, player_choice, computer_choice
    player_number = name_to_number(guess)
    comp_number = random.randrange(4)
    difference = (player_number - comp_number)%5
    
    player_choice = "Player: " + guess
    computer_choice = "Computer: " + str(number_to_name(comp_number))

    if difference == 0:
        result = "Player and Computer tie!"
    elif difference == 1 or difference == 2:
        result = "Player wins!"
    else:
        result = "Computer wins!"
    return result


def draw(canvas):
    global values
    canvas.draw_text("Pick One:", [WIDTH/2-70, 50], 24, "White")
    for item in values:
        size = int(WIDTH/5)
        i = values.index(item)
        canvas.draw_text(item.upper(), [size*i, 150], 24, "White")
    canvas.draw_text(player_choice, [WIDTH/4-70, 225], 24, "White")
    canvas.draw_text(computer_choice, [2*(WIDTH/4)+70, 225], 24, "White")
    canvas.draw_text(result, [WIDTH/4, 300], 40, "White")
    
def mouseclick(pos):
    for choice in values:
        size = int(WIDTH/5)
        i = values.index(choice)
        if i*size < pos[0] < (i+1)*size and 115 < pos[1] < 165:
            rpsls(choice)



frame = simplegui.create_frame("RPSLS", WIDTH, HEIGHT)
frame.set_canvas_background("Blue")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)


init()
frame.start()