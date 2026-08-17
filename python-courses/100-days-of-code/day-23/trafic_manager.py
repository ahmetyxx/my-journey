from car import Car
from turtle import Turtle, color
import random as r
import car

MAX_CAR_PER_STRİP=9
CAR_SPAWN_RANGE=40

class Manager:
    def __init__(self, xlen, ylen):
        self.car_speed = 8
        self.level = 1
        self.screen_xlen=xlen
        self.screen_ylen=ylen
        self.cars = []
        self.strips = []
        self.available_strips = []
        self.create_strips(ylen)

    def open_strips(self):

        for strip_ycor in self.strips:
            
            car_count = 0
            for car_obj in self.cars:
                if round(car_obj.ycor()) == strip_ycor:
                    car_count += 1

            if car_count >= MAX_CAR_PER_STRİP:
                if strip_ycor in self.available_strips:
                    self.available_strips.remove(strip_ycor)
                # else:
                #     print("we want to delete it but its not in avaliable strips?")

            elif car_count < MAX_CAR_PER_STRİP and strip_ycor not in self.available_strips:
                self.available_strips.append(strip_ycor)

    def draw_cars(self):
        if self.available_strips == []:
            return
        strip = r.choice(self.available_strips)
        x_pos = r.randint(self.screen_xlen//2,self.screen_xlen//2+CAR_SPAWN_RANGE)
        
        jhan = Car(x_pos, strip)
        self.cars.append(jhan)
        
    def move_cars(self):
        for car in self.cars:
            car.fd(self.car_speed)

    def garbage_killer(self):
        for car in self.cars[:]:
            if car.xcor()<-self.screen_xlen//2-15:
                car.ht()
                self.cars.remove(car)
                
    
    def create_strips(self, y_len):
        a = (-y_len // 2) + 100
        while a < y_len:
            self.strips.append(a)
            a += 50
        self.available_strips=self.strips.copy()
        
