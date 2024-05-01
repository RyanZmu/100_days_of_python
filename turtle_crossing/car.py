from turtle import Turtle
from random import randint, choice

# Screen boundaries
MAX_X = 600
MIN_X = -600
MAX_Y = 300
MIN_Y = -300

class Cars():
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_cars()
        self.crashed = False
        self.current_speed = 0.2


    def create_cars(self):
        # Make ten cars
        for _ in range(0,9):
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len= 4, stretch_wid= 2)
            car.setheading(180)
            car.speed(0)
            car.penup()

            # Pick a random color
            colors = ["red", "blue", "green", "yellow", "orange"]
            car.color(choice(colors))

            # Spawn car off screen in a random y coord and append to cars []
            car.teleport(x= randint(MIN_X, MAX_X), y=randint(MIN_Y, MAX_Y))
            self.cars.append(car)

        print(self.cars)


    def move_cars(self, player):
        for car in self.cars:
            if car.xcor() > MIN_X:
                car.goto(x= car.xcor()-self.current_speed, y= car.ycor())
            else:
                car.teleport(x= MAX_X, y=randint(MIN_Y, MAX_Y))
            self.check_collision(car, player)


    def check_collision(self, car, player):
        if car.distance(player) < 35:
            self.crashed = True
        return self.crashed
