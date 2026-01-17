from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.carros = []
        self.velocidad=STARTING_MOVE_DISTANCE

    def crear_carro(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            carro=Turtle()
            carro.color(random.choice(COLORS))
            carro.shape("square")
            carro.shapesize(stretch_wid=1,stretch_len=2)
            carro.penup()
            random_y=random.randint(-250,250)
            carro.goto(300,random_y)
            self.carros.append(carro)

    def mover(self):
        for nuevo_carro in self.carros:
            nuevo_carro.backward(self.velocidad)

    def mas_veloz(self):
        self.velocidad+=MOVE_INCREMENT










