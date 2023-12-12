from turtle import Turtle

FONT = ('Arial', 18, 'bold')


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.score
        self.upadate_score()

    def upadate_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align='center', font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.upadate_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.upadate_score() 

