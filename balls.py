from turtle import Turtle


class Ball(Turtle):



    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(10)
        self.x_move = 5  # MAX 9 
        self.y_move = -5  # MAX 9
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def upper_wall(self):
        print("The ball touched the upper wall")
        self.y_move *= -1
    
    def lower_wall(self):
        print("The ball touched the lower wall")
        self.y_move *= -1

    def left_wall(self):
        print("The ball touched the left side wall")
        self.x_move *= -1

    def right_wall(self):
        print("The ball touched the right side wall")
        self.x_move *= -1

    def player1_bounce(self):
        print("The ball bounced player 1")
        self.x_move *= -1
    
    def player2_bounce(self):
        print("The ball bounced player 2")
        self.x_move *= -1

    def get_my_coor(self):
        print(f"The current coordinates are {self.xcor()} , {self.ycor()}")




