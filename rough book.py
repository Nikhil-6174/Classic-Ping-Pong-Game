 
import turtle

import math



# Create two turtles
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

# Set positions of the turtles
turtle1.goto(100, 100)
turtle2.goto(200, 200)

# Get positions of the turtles
x1, y1 = turtle1.position()
x2, y2 = turtle2.position()

# Calculate the angle between the turtles
angle = math.degrees(math.atan2(y2 - y1, x2 - x1))

print(f"The angle between the two turtles is {angle} degrees.")

