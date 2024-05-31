from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue" , "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.current_moving_distance = STARTING_MOVE_DISTANCE
    
    def createCar(self):
        """Initializes a car at random y location"""
        random_chance = random.randint(1,8)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def moveCar(self):
        """Moves the car at a certain speed"""
        for car in self.all_cars:
            car.backward(self.current_moving_distance)
    
    def increaseCarSpeed(self):
        """Increases the spped of the car upon increment in levels"""
        self.current_moving_distance += MOVE_INCREMENT
