from turtle import Screen
from random import randint
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

def main():
    screen = Screen()
    screen.setup(800,600)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.title("Ping Pong Game")
    screen.listen()
    
    game_is_on = True
    r_paddle = Paddle((350,0))
    l_paddle = Paddle((-350,0))
    ball = Ball()
    score = Score()
    
    screen.onkeypress(r_paddle.up,"Up")
    screen.onkeypress(r_paddle.down,"Down")
    screen.onkeypress(l_paddle.up,"w")    
    screen.onkeypress(l_paddle.down,"s")
    
    while game_is_on:
        score.score_update(ball.index)
        screen.update()
        time.sleep(0.02)
        
        ball.move()
        
        #collision with paddle
        for i in range(len(r_paddle.body)):
            if ball.distance(r_paddle.body[i]) <20:
                ball.del_x = -5
                break
            
            elif ball.distance(l_paddle.body[i]) <20:
                ball.del_x = 5
                break
    screen.exitonclick()

if __name__ == "__main__":
    main()