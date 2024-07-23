from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, co_ordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(co_ordinate)

    def up(self):
        self.y_cor=self.ycor()
        self.goto(self.xcor(),self.y_cor+30)

    def down(self):
        self.y_cor=self.ycor()
        self.goto(self.xcor(),self.y_cor-30)

        