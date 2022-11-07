from turtle import Turtle, Screen
import random

is_race_on = False
colors = ["red", "blue", "green", "yellow", "orange", "violet", "black", "grey"]
y_positions = [-130, -100, -70, -40, 0, 40, 70, 100]
all_turtles = []
# tim = Turtle("turtle")
screen = Screen()
user_in = screen.textinput(title="Who will win?", prompt="Pick which turtle will win the race")

screen.setup(width=500, height=400)


for ninja_turtles in range(0, 8):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[ninja_turtles])
    new_turtle.goto(x=-230, y=y_positions[ninja_turtles])
    all_turtles.append(new_turtle)

if user_in:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            # for a window of 500x400, and a turtle size of 40x40, if a turtle reaches 230 it has won
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_in:
                print(f"You've won!, the {winning_color} turtle is the winner")
            else:
                print(f"You've lost!, the {winning_color} turtle is the winner")

        random_distance = random.randint(0, 30)
        turtle.forward(random_distance)

screen.exitonclick()
