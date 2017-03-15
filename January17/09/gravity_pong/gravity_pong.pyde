#TODO:
    # make GravityWell class
    # implement as array in game class
    # add "level" file that gets loaded, so we can place wells outside of code

from KeyState import * 
from Paddle import *
from Game import *
from Scoreboard import *

def setup():
    size(400,400)
    background(0)
    frameRate(60)
    
    global g
    CreateKeyState([UP,DOWN,LEFT,RIGHT])
    
    p1 = Paddle(20,height/2,10,50)
    p2 = Paddle(width-20,height/2,10,50)
    score = Scoreboard(10)
    
    g = Game(p1, p2, score)
    pass
    
def draw():
    global g
    background(0)
    g.update()
    g.draw()
    pass