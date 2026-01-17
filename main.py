import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
contador=0
jugador=Player()
car_manager = CarManager()

screen.listen()
screen.onkey(jugador.move_up, "Up")
game_is_on = True

nivel=Scoreboard()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.crear_carro()
    car_manager.mover()
    for carro in car_manager.carros:
        if jugador.distance(carro)<20:
            game_is_on=False
            nivel.perdio()

    if jugador.ycor()>280:
        jugador.inicio()
        car_manager.mas_veloz()
        nivel.gano()
print(car_manager.carros)
screen.exitonclick()




