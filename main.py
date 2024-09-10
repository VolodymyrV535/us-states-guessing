import turtle
import pandas as pd


STATES_AMOUNT = 50

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# define turtle to write text
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

# the code to get coordinates for each state location (disabled when you have all the data)
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

answers_amount = 0
guessed_states = []

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

while answers_amount < STATES_AMOUNT:
    
    df = pd.read_csv("./50_states.csv")

    check_state_df = df[df["state"] == answer_state]

    if answer_state == "Exit":
        break
    
    if not check_state_df.empty:
        x_coor = check_state_df.x.item()
        y_coor = check_state_df.y.item()
        writer.goto(x_coor, y_coor)
        writer.write(answer_state, font=("Times New Roman", 10, "normal"))
        
        answers_amount += 1
        guessed_states.append(answer_state)
        
    else:
        pass
    
    answer_state = screen.textinput(title=f"{answers_amount}/{STATES_AMOUNT} States Correct", prompt="What's another state's name?").title()
    
# states_to_learn.csv
missed_states = []

all_states = df.state.to_list()
for each_state in all_states:
    if each_state not in guessed_states:
        missed_states.append(each_state)
    
# with open ("states_to_learn.csv", "a") as missed_file:
#     for state in missed_states:
#         missed_file.write(f"{state}\n")

output_dataframe = pd.DataFrame({"missed states": missed_states})

output_dataframe.to_csv("states_to_learn.csv", index=False)
        