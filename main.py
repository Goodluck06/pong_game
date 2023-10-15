from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboad import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Danii")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# I am sending you 1π! Pi is a new digital currency developed by Stanford PhDs, with over 47 million members worldwide. To claim your Pi, follow this link https://minepi.com/MissHerieth and use my username (MissHerieth) as your invitation code.

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collition with the wall
    if ball.ycor()>270 or ball.ycor()<-270:
        ball.bounce_y()

    # Detect if ball made contact with tha paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()