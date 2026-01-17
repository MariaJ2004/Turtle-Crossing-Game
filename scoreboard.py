from turtle import *
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-280, 250)
        self.level=1
        self.write(f"Level={self.level} ", align="center", font=FONT)
        self.hideturtle()

    def gano(self):
        self.level+=1
        self.clear()
        self.write(f"Level={self.level} ", align="center", font=FONT)

    def perdio(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)





