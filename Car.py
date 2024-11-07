class Car:
    def __init__(self, make, model, year, speed=0):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, value):
        self.__make = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def speed(self):
        return self.__speed

    def increase_speed(self):
        self.__speed += 5

    def decrease_speed(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def stop(self):
        self.__speed = 0

    def display_speed(self):
        return f"Current speed: {self.__speed} km/h"

    def turn(self):
        self.__speed = -self.__speed

car = Car("Mitsubishi", "Eclipse", 2001)
car.increase_speed()
print(car.display_speed())
car.increase_speed()
print(car.display_speed())
car.decrease_speed()
print(car.display_speed())
car.stop()
print(car.display_speed())
car.turn()
print(car.display_speed())