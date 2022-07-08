from turtle import Turtle

FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0

    def write_state_name(self, name, x, y):
        self.goto(x, y)
        self.write(name, align=ALIGNMENT, font=FONT)
        self.score += 1
