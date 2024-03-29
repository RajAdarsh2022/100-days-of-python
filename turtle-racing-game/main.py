import turtle
import random


screen = turtle.Screen()
screen.screensize(canvheight = 400, canvwidth = 500)
user_bet = screen.textinput(title = "Make your bet" , prompt= "Which turtle you think would win the race?" )

#Creating 5 instances of the turtle object
turtle_colors = ["purple", "green", "yellow", "orange", "red"]
turtles = []

for index in range(len(turtle_colors)):
    t = turtle.Turtle(shape = "turtle")
    t.color(turtle_colors[index])
    t.penup()
    turtles.append(t)

# Positioning all the turtles at the starting line
vertical_distance = 50
horizontal_location = -400
for index in range(len(turtles)):
    t = turtles[index]
    t.setpos(x= horizontal_location, y= 100-vertical_distance*index)

#Starting the race
is_race_on = True
while is_race_on:
    for t in turtles:
        moving_distance = random.randint(0, 10)
        t.fd(moving_distance)

        #checking if the turtle has reached finished line
        if t.xcor() >= 450:
            winner = t.color()[0]
            is_race_on = False
            break

#Cheking if the user guess is correct or not
if winner == user_bet:
    print(f"Your bet was correct! {winner} turtle won the race.")
else:
    print(f"Your lose! {winner} turtle won the race.")


screen.exitonclick()