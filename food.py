from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('darksalmon')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-420, 420)
        random_y = random.randint(-300, 300)
        self.goto(random_x, random_y)