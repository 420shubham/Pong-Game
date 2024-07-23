from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x_move=10
        self.y_move=10       #comments are changes that can be made on how you choose to move the ball
                            #self.setheading(random.choice([list of directions]))
   
   
   
    def move(self):
        new_x=self.xcor() + self.x_move  #self.forward(10)
        new_y=self.ycor() + self.y_move

        self.goto(x=new_x,y=new_y)

    def reflect_wall(self):     
        self.y_move *= -1           #setheading(360-self.heading())

    def reflect_paddle(self):
        self.x_move *= -1            #setheading(180-self.heading())

    def change_direction(self):
        self.x_move *= -1
