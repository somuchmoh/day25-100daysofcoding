import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
data = pandas.read_csv("50_states.csv")
score = 0
game_is_on = True

while game_is_on:
    answer = screen.textinput(title="Guess the State", prompt="Name a state")
    state = data['state'].eq(answer.title()).any()
    state_index = data[data['state'] == answer.title()].index.values
    state_x = data.at[state_index[0], 'x']
    state_y = data.at[state_index[0], 'y']
    if state:
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(state_x, state_y)
        turtle.write(f"{answer.title()}", align='center', font=('Arial', 10, 'bold'))
        score += 1
        screen.title(f"{score}/50 - U.S. States Game")
    else:
        print(f"Your final states count = {score}/50")


screen.exitonclick()
