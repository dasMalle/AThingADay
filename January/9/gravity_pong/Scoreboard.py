class Scoreboard():
    def __init__(self, maxScore):
        self.scores = [0,0]
        self.maxScore = maxScore
        
    def AddScore(self,player):
        self.scores[player-1] += 1
        if self.scores[player-1] == self.maxScore:
            return True
        return False
    
    def draw(self):
        textAlign(LEFT)
        text("Score: "+str(self.scores[0]), 10, 10);
        textAlign(RIGHT)
        text("Score: "+str(self.scores[1]), width-10, 10);
        pass