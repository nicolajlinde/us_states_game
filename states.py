from turtle import Turtle

FONT = ("Courier", 8, "normal")
ALIGNMENT = "center"


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state_name(self, name, x, y):
        self.goto(x, y)
        self.write(name, align=ALIGNMENT, font=FONT)
