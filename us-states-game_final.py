import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 states correct.", prompt="Name a state").title()
    print(answer_state)

    if answer_state == "Exit":
        break
    if answer_state.title() in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

states_to_learn = [state for state in all_states if state not in guess_states]
# for state in all_states:
#     if state not in guess_states:
#         states_to_learn.append(state)

new_file = pandas.DataFrame(states_to_learn)
with open("states_to_learn.csv", mode='w') as new_data:
    new_data.write(new_file.to_csv())

screen.exitonclick()
