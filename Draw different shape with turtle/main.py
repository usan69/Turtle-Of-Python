import turtle as t
import random

t.colormode(260)
siu=t.Turtle()
siu.pensize(10)




#num=5
colours=["IndianRed","DarkOrchid","DeepSkyBlue"]

def draw_shape(num):
    angle=360/num
    for _ in range(num):
        siu.forward(100)
        siu.right(angle)


for shape in range(3,11):
    siu.color(random.choice(colours))
    draw_shape(shape)