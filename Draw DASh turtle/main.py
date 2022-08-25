from turtle import Turtle, Screen

siu=Turtle()
dis=Screen()
for _ in range(10):
    siu.forward(10)
    siu.penup()
    siu.forward(10)
    siu.pendown()

dis.exitonclick()
