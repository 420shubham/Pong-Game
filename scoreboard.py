from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("yellow")
        self.speed(0)
        self.pu()
        self.r_score=0
        self.l_score=0

        
    def center_line(self):
        self.goto(0,300)
        self.setheading(270)

        for i in range(30):
            self.pd()
            self.fd(10)
            self.pu()
            self.fd(10)
            
    
    def print_score(self,score):
        self.write(f"SCORE= {score}", False, "center", ("Comic Sans MS",24,"bold"))

    def show_score(self):
        self.clear()
        self.center_line()

        self.goto(150,240)
        self.print_score(self.r_score)
        self.goto(-150,240)
        self.print_score(self.l_score)

    def update_score(self,r_or_l):
        if r_or_l=="R":
            self.r_score +=  1
        else:
            self.l_score += 1
    





                   
