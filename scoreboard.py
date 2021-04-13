from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-20,230)
        self.write("SCORE\n{} | {}".format(self.l_score,self.r_score),False,ALIGNMENT,FONT)
    
    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0,70)
        self.write("GAME OVER\nScore: {}".format(self.score),False,ALIGNMENT,FONT)
    
    def score_update(self,points=(0,0)):
        self.l_score += points[0]
        self.r_score += points[1]
        self.clear()
        self.write("SCORE\n{} | {}".format(self.l_score,self.r_score),False,ALIGNMENT,FONT)