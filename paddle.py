from turtle import Turtle
PADDLE_WIDTH =20
PADDLE_HEIGHT = 100
PADDLE_X = 350
PADDLE_Y = 0
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self,position=(0,0)):
        self.body = []
        self.create_paddle(position)
        self.top = self.body[0]
        self.bottom = self.body[-1]
    
    def create_paddle(self,position,color = "white"):
        for i in range(int(PADDLE_HEIGHT/PADDLE_WIDTH)):
            segment = Turtle()
            segment.shape("square")
            segment.color(color)
            segment.pu()
            if len(self.body) == 0:
                segment.goto(position)
            else:
                segment.goto(self.body[i-1].xcor(), self.body[i-1].ycor() -20)
            self.body.append(segment)
            
    def up(self):
        if self.top.ycor() < 280:
            for seg in range(len(self.body)-1,0,-1):
                new_x = self.body[seg-1].xcor()
                new_y = self.body[seg-1].ycor()
                self.body[seg].goto(new_x,new_y)
            self.top.setheading(90)
            self.top.forward(MOVE_DISTANCE)
    
    def down(self):
        if self.bottom.ycor() > -280:
            for seg in range(0,len(self.body)-1):
                new_x = self.body[seg+1].xcor()
                new_y = self.body[seg+1].ycor()
                self.body[seg].goto(new_x,new_y)
            self.bottom.setheading(270)
            self.bottom.forward(MOVE_DISTANCE)
        