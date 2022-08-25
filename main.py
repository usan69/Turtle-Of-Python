from turtle import Turtle,Screen

siu_turtle=Turtle()
my_screen=Screen()
for _ in range(4):
    siu_turtle.forward(100)
    siu_turtle.left(90)

my_screen.exitonclick()


#importing modules

import heroes
print(heroes.gen())

import villains
print(villains.gen())





