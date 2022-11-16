import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the State!")
us_map = "blank_states_img.gif"
screen.addshape(us_map)
turtle.shape(us_map)

data = pandas.read_csv("50_states.csv")

all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States", prompt="Whats another state?").title()

    if answer_state == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        print(new_data)
        new_data.to_csv("missing_states.csv")
        print(missing_states)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.color("black")
        x_cor = int(data["x"][data["state"] == answer_state])
        y_cor = int(data["y"][data["state"] == answer_state])
        state_turtle.goto(x=x_cor, y=y_cor)
        state_turtle.write(answer_state, True, align="center")


turtle.mainloop()
