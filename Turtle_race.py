import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Pick a colour: ")

all_turtles = []
color = ["red", "blue" , "green", "yellow", "black", "orange",]

race_on = False
spacing = -90
for index, color_name in enumerate(color):
    new_turtle = Turtle("turtle")
    new_turtle.color(color_name)
    new_turtle.pu()
    new_turtle.goto(x= -230, y = -90 + index * 40)
    all_turtles.append(new_turtle)
    spacing+=40

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"🎉 You've won! The {winning_color} turtle won the race!")
            else:
                print(f"😢 You lost. The {winning_color} turtle won the race.")
        turtle.fd(random.randint(0,10))

screen.exitonclick()