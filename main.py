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
all_states = data.state.to_list()
state_len = len(data.state)
correct_guesses = []

game_is_on = True
while game_is_on:
    guess = screen.textinput(title=f"{len(correct_guesses)}/{state_len}Guess the State", prompt="What's another state's name?").title()

    if guess == "Quit" or guess == "Exit":
        game_is_on = False
        screen.bye()
    elif guess in correct_guesses:
        print("You've already guessed that. Try again.")
    elif guess in all_states:
        row = data[data.state == guess]
        state.write_state_name(guess, float(row.x), float(row.y))
        correct_guesses.append(guess)
    else:
        print("Sorry, there aren't any states of that name. Maybe you misspelled or forgot an uppercase letter?")

    if len(correct_guesses) >= state_len:
        print("Congratulation you won! You guessed all 50 states.")
        game_is_on = False

turtle.exitonclick()
