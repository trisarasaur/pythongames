import simplegui

RADIUS = 20
color = "White"
w = "White"
b = "Black"
board = [[w,w,w,w,w],
        [w,w,b,w,w],
        [w,w,b,w,w],
        [w,w,b,w,w],
        [w,w,w,w,w]]

def draw(canvas):
    
    for y in range(1,6):
        for x in range(1,6):
            canvas.draw_circle([x*50,y*50], RADIUS, 10, board[y-1][x-1], board[y-1][x-1])
def neighbors(x,y):
    neighbors = []
    count = 0
    for y1 in range(y-1,y+2):
        for x1 in range (x-1,x+2):
            if not(y1 == y and x1 == x) and x1>=0 and y1>=0 and x1<5 and y1<5:
                if board[y1][x1] == b:
                    count +=1
    return count

def tick():
    global board
    new_board =[]
    for y in range(0,5):
        new_row = [] 
        new_board.append(new_row)
        for x in range(0,5):
            n_count = neighbors(x, y)
            if n_count < 2:
                new_row.append(w)
            elif n_count == 2: 
                new_row.append(board[y][x])
            elif n_count == 3:
                new_row.append(b)
            else: 
                new_row.append(w)
    board = new_board    
    print 'tick'


frame = simplegui.create_frame("Game of Life", 300, 300)
frame.set_canvas_background("Blue")

timer = simplegui.create_timer(1000, tick)
frame.set_draw_handler(draw)

frame.start()
timer.start()