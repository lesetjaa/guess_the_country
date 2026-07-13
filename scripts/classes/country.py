from turtle import Turtle

FONT = ("Courier", 8, "normal")


class Country(Turtle):

    def __init__(self, name: str, coord: tuple) -> None:
        super().__init__(visible=False, shape="square")
        self.penup()
        self.goto(coord)
        self.write(name, font=FONT, align="center")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
