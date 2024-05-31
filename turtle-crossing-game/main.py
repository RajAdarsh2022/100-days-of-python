import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Adding event listeners
screen.onkey(player.moveUp , "Up")
screen.onkey(player.moveDown , "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.createCar()
    car_manager.moveCar()

    #Detecting collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    #Detecting succesful crossing
    if player.isAtFinishLine():
        player.reset()
        car_manager.increaseCarSpeed()
        scoreboard.increaseLevel()


scoreboard.gameOver()
screen.exitonclick()
