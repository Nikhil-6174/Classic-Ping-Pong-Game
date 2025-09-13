from turtle import Turtle,Screen
from Paddle import Player
from balls import Ball
from score import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.screensize(800,600)
screen.delay(1)

# boundary drawing

boundary = Turtle()
boundary.ht()
boundary.penup()
boundary.pencolor("white")
boundary.goto(400,-300)
boundary.pendown()
boundary.seth(90)
boundary.speed(0)

for x in range(2):
    boundary.fd(600)
    boundary.left(90)
    boundary.fd(800)
    boundary.left(90)

boundary.up()

# umpire

umpire = Scoreboard()
umpire.prt_score()

# players

player_1 = Player()
player_1.go_2(-385,0)

player_2 = Player()
player_2.go_2(385,0)

# players movement

screen.listen()
screen.onkeypress(player_1.go_up,"w")
screen.onkeypress(player_1.go_down,"s")
screen.onkeypress(player_2.go_up,"Up")
screen.onkeypress(player_2.go_down,"Down")

#to create a ball

ping = Ball()

while -400 < ping.xcor() < 400 and -300 < ping.ycor() < 300:

    ping.move()

    # this is to ge the ball bouncing all arround

    if ping.xcor() > 390 :
        ping.right_wall()
        ping.get_my_coor()
        umpire.up_p1()
        umpire.refresh_score()

    if ping.xcor() < -390:
        ping.left_wall()
        ping.get_my_coor()
        umpire.up_p2()
        umpire.refresh_score()

    if ping.ycor() > 290:
        ping.upper_wall()
        ping.get_my_coor()

    if ping.ycor() < -290:
        ping.lower_wall()
        ping.get_my_coor()
    
    # to detect collision with players

    if ((player_1.ycor() - 35)  < ping.ycor() < (player_1.ycor() + 25)) and ping.xcor() > 365:
        ping.player1_bounce()

    if ((player_2.ycor() - 35)  < ping.ycor() < (player_2.ycor() + 25)) and ping.xcor() < -365:
        ping.player2_bounce()

    # if ping.distance(player_1) < 35 : #and ping.xcor() > 363
    #     ping.player1_bounce()
    #     ping.get_my_coor()

    # elif ping.distance(player_2) < 35 : #and ping.xcor() < -363
    #     ping.player2_bounce()   
    #     ping.get_my_coor()
    
    if umpire.p1s == umpire.bestof:
        umpire.goto(0,0)
        umpire.winner("Player 1")
        break
    elif umpire.p2s == umpire.bestof:
        umpire.goto(0,0)
        umpire.winner("Player 2")
        break

screen.exitonclick()