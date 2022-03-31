import turtle
from turtle import Turtle,Screen
import random

tim = Turtle()
screen = Screen()
tim.speed("fastest")
a = int(input("Enter Number of Circles:"))
b = int(input("Enter the Radius Of Circle:"))

screen.colormode(255)
angle = 350/a

def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for i in range(1,a+1):
    tim.pencolor(random_rgb())
    tim.circle(b)
    tim.setheading(i*angle)


screen.exitonclick()
