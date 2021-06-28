from graphics import *
import time, random


win = GraphWin('Snake', 600, 600) #this is the window
win.setBackground('black')

player = Rectangle(Point(0,0), Point(10,10))
#player.setOutline('white')
player.setFill('purple')
player.draw(win)


x = y = 0 #for p_movement()
prev_player_pos = []
tail_length = 0
clones = []
fruit_pos = None
generated = False #for fruit_gen()
fruit = None
lost = False


def p_movement():
    global player, x, y
    time.sleep(.08)
    player.move(x, y)
    pinput = win.checkKey()
    if pinput == 'd':
        x, y = 10, 0
    if pinput == 'a':
        x, y = -10, 0
    if pinput == 'w':
        x, y = 0, -10
    if pinput == 's':
        x, y = 0, 10


def prev_player_pos_fun():
    global prev_player_pos, tail_length
    prev_player_pos.append(player.getP1())
    if len(prev_player_pos) > tail_length + 1:
        prev_player_pos.pop(0)
    

def tail():
    global tail_length, clones
    x = player.clone().draw(win)
    clones.append(x)
    if tail_length + 1 < len(clones):       # I think this works
        clones[0].undraw()
        clones.pop(0)

def fruit_gen():
    global prev_player_pos, fruit_pos, generated, fruit
    while generated == False:
        x = random.choice(range(0,60))
        y = random.choice(range(0,60))
        trying = Point(x * 10, y * 10)
        if trying not in prev_player_pos:
            fruit = Rectangle(Point(x * 10, y * 10), Point(x * 10 + 10, y * 10 + 10))
            fruit.setFill('yellow')
            fruit.draw(win)
            fruit_pos = fruit.getP1()
            generated = True


def fruit_eaten():
    global prev_player_pos, fruit_pos, tail_length, fruit, generated
    if str(prev_player_pos[-1]) == str(fruit_pos):
        tail_length = tail_length + 1
        generated = False
        fruit.undraw()


def dying():
    global prev_player_pos, lost
    i = 0
    while len(prev_player_pos) - 1 > i:
        if str(prev_player_pos[i]) == str(prev_player_pos[-1]):
            print('you lose')
            lost = True
            break
        else:
            i = i + 1

    
def main():
    global player
    while True:
        prev_player_pos_fun()
        p_movement()
        tail()
        fruit_gen()
        fruit_eaten()
        dying()
        if lost == True:
            break


main()
