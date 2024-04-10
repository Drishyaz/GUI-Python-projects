import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.move_turtle)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Update and Show the Levels every time at the beginning of the game
    scoreboard.update_board()

    # Create and move the cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect turtle's collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if player reaches top edge of screen
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_car_speed()
        scoreboard.increase_level()

screen.exitonclick()
