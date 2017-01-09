from KeyState import *

class Paddle():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        pass
    
    def draw(self):
        rectMode(CENTER)
        fill(255,255,255,255)
        rect(self.x,self.y,self.w,self.h)
        pass
        
    def doControls(self):
        keyState = GetKeyState()
        if keyState.isDown(DOWN):
            self.y += 2
        elif keyState.isDown(UP):
            self.y -= 2
        pass
    
    def doAI(self, ball):
        if ball.y > self.y + self.w / 2:
            self.y +=2
        elif ball.y < self.y - self.w / 2:
            self.y -= 2
        pass