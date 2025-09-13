from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shapesize(0.001)
        self.goto(0,320)
        self.p1s = 0
        self.p2s = 0
        self.bestof = 66 # this is to define game end point 
        
    def prt_score(self):
        self.write(f"Player - 1: {self.p1s} | Player - 2: {self.p2s} ", align= "center",font=('Arial', 20, 'normal'))

    def winner(self,name):
        self.write(f"{name} won the game!",align= "center",font=('Arial', 20, 'normal'))

    def refresh_score(self):
        self.clear()
        self.prt_score()

    def up_p1(self):
        self.p1s += 1

    def up_p2(self):
        self.p2s += 1
