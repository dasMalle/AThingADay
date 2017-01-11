import KeyState
from Ball import *

class Game():
    def __init__(self, p1, p2, scoreboard):
        self.p1 = p1
        self.p2 = p2
        self.scoreboard = scoreboard
        self.state = 0
        self.timer = 0
        self.ball = Ball(width/2,height/2, 10, [random(0,1),random(0,1)])
        self.distOffset = 0
        pass
    
    def update(self):
        if self.state == 0:
            scoreCheck = self.ball.update()
            
            if scoreCheck != 0:
                if self.scoreboard.AddScore(scoreCheck):
                    #todo: game over!
                    pass
            
            self.p1.doControls()
            self.p2.doAI(self.ball)
            
            self.ball.doCollision(self.p1)
            self.ball.doCollision(self.p2)
            pass
        elif self.state == 1:
            #timer for reset
            pass
        elif self.state == 2:
            #handle reset / quit buttons
            pass
        pass
        
    def draw(self):
        self.p1.draw()
        self.p2.draw()
        if self.state == 0:
            self.ball.draw()
        
        self.scoreboard.draw()
        self.drawGravity()
        pass
        
    def drawGravity(self):
        self.distOffset -= 1
        for i in range(0,10):
            self.doCircle(i * 20 + self.distOffset, 1)
        pass
        
    def doCircle(self, distance, distScale):
        while distance < 0:
            distance += 200
        a = 200 - distance
        noFill()
        stroke( 255, 255, 255, a )
        ellipse(width/2, height/2, distance, distance)