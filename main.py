from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car_create()
    car_manager.move_cars()

    #Deteksi benturan dengan turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Deteksi ketika turtle sampai garis depan, kondisi akan mulai dari titik awal dan speed menambah
    if player.is_at_finish_line():
        player.go_to_statrt()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()