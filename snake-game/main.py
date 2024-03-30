import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


#Creating the screen with desired inputs
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


#Creating the snake, food and scoreboard object
my_snake = Snake()
snake_food = Food()
game_scoreboard = Scoreboard()
screen.update()

#Adding key bindings/ event listeners to the screen
screen.listen()
screen.onkey(my_snake.up , "Up")
screen.onkey(my_snake.down , "Down")
screen.onkey(my_snake.left , "Left")
screen.onkey(my_snake.right , "Right")


#Creating the snake movement
is_game_on = True
while is_game_on:
    my_snake.move_forward()
    screen.update()
    time.sleep(0.1)

    #Checking for the collision between snake and the food
    if snake_food.distance(my_snake.snake_head) <= 15:
        #Increasing the score and displaying it in scoreboard
        game_scoreboard.score += 1
        game_scoreboard.display_score()
        #Increasing the length of the snake
        my_snake.extend()
        #Respawning the food at a random location
        snake_food.spawn()
    
    #Detect collison with tail
    #if head collides with any segment in the tail, then game over !
    for segment in my_snake.snake_segments:
        if segment != my_snake.snake_head:
            if my_snake.snake_head.distance(segment) < 5:
                is_game_on = False
                game_scoreboard.game_over()

screen.exitonclick()