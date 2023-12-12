from turtle import Turtle
import random

COLORS = ["pink", "yellow", "green", "blue", "red", "purple", "white", "brown"] 

class Food(Turtle):

    def __init__(self):
       super().__init__() 
       self.shape("circle")
       self.penup()
       self.shapesize(stretch_len=0.5,stretch_wid=0.5)
       random_color = random.choice(COLORS)
       self.color(random_color)
       self.speed("fastest")
       self.refresh()

    def refresh(self):
       random_x = random.randint(-270,270)
       random_y = random.randint(-270,270)
       self.goto(random_x, random_y)
       random_color = random.choice(COLORS)
       self.color(random_color)

      