import turtle
import pandas
from states import State


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state = State()

data = pandas.read_csv("50_states.csv")
state_len = len(data.state)
correct_guesses = []

game_is_on = True
while game_is_on:
    guess = screen.textinput(title=f"{state.score}/{state_len}Guess the State", prompt="What's another state's name?").title()

    for i in data.state:
        if guess == i:
            row = data[data.state == i]
            state.write_state_name(i, float(row.x), float(row.y))
            correct_guesses.append(guess)

        if len(correct_guesses) == state_len:
            print("Congratulation you won! You guessed all 50 states.")
            game_is_on = False

turtle.mainloop()
