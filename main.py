from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = ScoreBoard()


game_on = True
while game_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    screen.onkey(key="d", fun=snake.right)
    screen.onkey(key="a", fun=snake.left)
    screen.onkey(key="w", fun=snake.up)
    screen.onkey(key="s", fun=snake.down)
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 17:
        food.refresh()
        score.increase_score()
        snake.grow()

    if snake.is_wall_hit() or snake.is_tail_hit():
        score.game_over()
        game_on = False

screen.exitonclick()
