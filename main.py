from turtle import Screen
import time
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Danii")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# I am sending you 1π! Pi is a new digital currency developed by Stanford PhDs, with over 47 million members worldwide. To claim your Pi, follow this link https://minepi.com/MissHerieth and use my username (MissHerieth) as your invitation code.

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor()==270 or ball.ycor()==-270:
        ball.bounce()
    if ball.xcor()==370 or ball.xcor()==-370:
        ball.bounce()








screen.exitonclick()