from turtle import Turtle


class Player(Turtle):     

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1,3,None)
        self.speed(0)

        
    def go_2(self,go_to_x,go_to_y):
        self.goto(go_to_x,go_to_y)
        self.right(90)
        self.color("white")
        
    def go_up(self):
        print(f"Red steped to {self.xcor()}, {self.ycor()}")
        self.bk(25)
        if self.xcor() > 0:
            if self.ycor() > 280:
                self.goto(385,280)
            elif self.ycor() < -280:
                self.goto(385,-280)
        elif self.xcor() < 0:
            if self.ycor() > 280:
                self.goto(-385,280)
            elif self.ycor() < -280:
                self.goto(385,-280)
            

    def go_down(self):
        print(f"Red steped to {self.xcor()}, {self.ycor()}")
        self.fd(25)
        if self.xcor() > 0:
            if self.ycor() > 280:
                self.goto(385,280)
            elif self.ycor() < -280:
                self.goto(385,-280)
        elif self.xcor() < 0:
            if self.ycor() > 280:
                self.goto(-385,280)
            elif self.ycor() < -280:
                self.goto(-385,-280)

            
        

        