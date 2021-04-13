from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.del_x = 5
        self.del_y = 5
        self.index = (0,0)
    
    def move(self):
        if self.ycor() == 285:
            self.del_y = -5
        
        elif self.ycor() ==-285:
            self.del_y = +5
        
        x_new = self.xcor() + self.del_x
        y_new = self.ycor() + self.del_y
        self.goto(x_new,y_new)
        self.index = (0,0)
        
        if x_new > 390:
            self.goto(0,0)
            self.index = (1,0)
        
        elif x_new < -390:
            self.goto(0,0)
            self.index = (0,1) 