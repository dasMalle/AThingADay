from Paddle import *

class Ball:
    def __init__(self, x, y, size, initialVelocity):
        self.x = x
        self.y = y
        self.speed = 2
        self.velocity = initialVelocity
        self.size = size
        self.addedSpeed = 0
    
    def update(self):
        #gravitational attraction to center of screen
        dx = (width/2) - self.x
        dy = (height/2) - self.y
        d = sqrt(dx * dx + dy * dy)
                
        #limit to min 25 units
        #so if the ball gets closer than 25 pixels, we'll act like it's 25 pixels away        
        if d <= 25.0:
            d = 25.0
            self.addedSpeed += 0.1
        else:
            self.addedSpeed = 0
            
        d = d * d * d
                
        fX = dx * ( 100 / d );
        fY = dy * ( 100 / d );
        
        self.velocity[0] += fX#sqrt(10.0/(xD*xD))
        self.velocity[1] += fY#sqrt(10.0/(yD*yD))
        
        #normalize velocity direction!
        l = sqrt( self.velocity[0] * self.velocity[0] + self.velocity[1] * self.velocity[1] );
        self.velocity[0] = self.velocity[0] / l
        self.velocity[1] = self.velocity[1] / l
        
        self.x += self.velocity[0] * ( self.speed + self.addedSpeed )
        self.y += self.velocity[1] * ( self.speed + self.addedSpeed )
        scored = 0
        if self.x > width - self.size / 2 or self.x < self.size / 2:
            if self.x < width / 2:
                scored = 2 #right scored
            else:
                scored = 1 #left scored
            self.x = width / 2
            self.y = height / 2
            self.velocity[0] *= -1
            self.velocity[1] = 0
            self.speed = 2
        if self.y > height - self.size / 2 or self.y < self.size / 2:
            self.velocity[1] *= -1
        return scored #nobody scored
        
    def draw(self):
        fill(255,255,255,255)
        ellipse(self.x,self.y,self.size,self.size)
        pass
        
    def doCollision(self, paddle):
        padRight = paddle.x + paddle.w / 2
        padLeft = paddle.x - paddle.w / 2
        ballRight = self.x + self.size / 2
        ballLeft = self.x - self.size / 2
        
        padTop = paddle.y + paddle.h / 2
        padBot = paddle.y - paddle.h / 2
        ballTop = self.y + self.size / 2
        ballBot = self.y - self.size / 2
        
        if padRight > ballLeft and padLeft < ballRight:
            if padTop > ballBot and padBot < ballTop:
                dirY = self.y - paddle.y
                if dirY > 1: dirY = 1
                if dirY < -1: dirY = -1
                self.velocity[0] = self.velocity[0] * -1
                self.velocity[1] = dirY
                self.speed += 0.1
                #snap ball to outside of paddle
                if self.x < paddle.x:
                    self.x = paddle.x - paddle.w / 2 - self.size / 2
                else:
                    self.x = paddle.x + paddle.w / 2 + self.size / 2
        