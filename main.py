from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake


# This block of code: 1. creates the screen 2. sets its height and width 3. changes the background color to black
# 4. names the screen popup 5. turns the animation off
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

score = Scoreboard()
# Created a new "snake" object
snake = Snake()
food = Food()

# Created an event listener that listens for keys to be clicked.
# This also provided functionality to our snake allowing it to move in whatever direction we tell it to.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Created a state variable to stop the while loop when necessary.
game_is_on = True

# This while loop allows our snake to move freely, but with a .1 ms delay for a smoother classic Snake feel.
while game_is_on:
    screen.update()
    time.sleep(0.1)
# This function is a part of our snake object and simultaneously moves all the blocks of our snake.
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()

        # If head collides with any segment in the tail:
            # Trigger game_over

screen.exitonclick()
