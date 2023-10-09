import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def write_image(x,y,answer_state):
    t= turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.write(f"{answer_state}")

guessed_states = []
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) <=50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 State","What's another state name?").title()
    print(answer_state)
    # Get data from the csv file
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        # missing_state = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        learn_data = pd.DataFrame(missing_state)
        break
    if answer_state in all_states == data.state.to_list():
        state_data = data[data['state'] == answer_state]
        write_image(int(state_data.x),int(state_data.y),state_data.state.item())
        guessed_states.append(answer_state)
    else:
        print("Invalid answer")

print("Learn Missing States",learn_data)

screen.exitonclick()