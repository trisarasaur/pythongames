# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def init():
    global cards, face_down, state, moves
    state = 0
    moves = 0
    l.set_text("Moves = "+str(moves))
    face_down = []
    i = 0
    while i < 16:
        face_down.append(True)
        i += 1
    cards = [i%8 for i in range(16)]
    random.shuffle(cards)
    print cards
     
# define event handlers
def mouseclick(pos):
    global state, first_index, second_index, moves
    i = 0
    for card in cards:
        x = i%4
        y = int(i/4)
        if 75*x < pos[0] < 75*(x+1) and 100*y < pos[1] < 100*(y+1):
            if face_down[i]:
                face_down[i] = False
                if state == 0:
                    first_index = i
                elif state == 1:
                    second_index = i
                    moves += 1
                    l.set_text("Moves = "+str(moves))
                elif state == 2:
                    if cards[second_index] == cards[first_index]:
                        pass
                    else:
                        face_down[second_index], face_down[first_index] = True, True
                    first_index = i
                    state = 0
                state += 1
            else:
                pass
        i += 1
                     
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards
    i = 0
    for card in cards:
        x = i%4
        y = int(i/4)
        if not face_down[i]:
            canvas.draw_text(str(card+1), [x*75+30, y*100+60], 26, "White")
        elif face_down[i]:
            canvas.draw_polygon([(x*75, y*100), ((x+1)*75, y*100), ((x+1)*75, (y+1)*100), (x*75,(y+1)*100)], 4, "White", "Green")
        i+=1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 300, 400)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
