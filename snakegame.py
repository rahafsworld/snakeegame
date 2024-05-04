from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("My Snakes Game")

border = Turtle()
border.penup()
border.goto(-440, -340)
border.pendown()
border.color("white")
border.pensize(3)
for _ in range(2):
    border.forward(880)
    border.left(90)
    border.forward(680)
    border.left(90)
border.hideturtle()

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if (
            snake.head.xcor() > 430
            or snake.head.xcor() < -430
            or snake.head.ycor() > 330
            or snake.head.ycor() < -330
    ):
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if segment in snake.segments:
            pass

        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            score.reset()

screen.exitonclick()