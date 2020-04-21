                        # task 1

from time import sleep
from intertools import cycle
class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 9))
        def running(self):
            for color, sec in cycle(self.__color):
                print(color, '(wait {} sec)'.format(sec))
                sleep(sec)
traffic_light = TrafficLight()
traffic_light.running()

                         # task 2

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def calc_mass(self):
        mass = self._lenght * self._width * 25 * 5 / 1000
        print(mass, 'т')
my_road = Road(20, 5000)
my_road.calc_mass()

                         # task 3

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']
class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname, self.position)
    def get_total_income(self):
        print(self._income_wage + self._income_bonus)
pos = Position('Max', 'Ilin', 'manager', {"wage": 70000, "bonus": 30000})
pos.get_full_name()
pos.get_total_income()

                          # task 4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('{} is going!'.format(self.name))
    def stop (self):
        print('{} is stoping!'.format(self.name))
    def turn(self, direction):
        print('{} is turning to {}!'format(self.name, direction))
    def show_speed(self):
        print('Current speed:', self.speed)
class TownCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 60:
            print('Warning! Your speed is more than max')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 40:
            print('Warnig! Your speed is more than max')


                          # task 5

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('Ручка рисует')
class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует')
class Handle(Stationery):
    def draw(self):
        print('Маркер рисует')
pen = Pen('ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
pen.draw()
pencil.draw()
handle.draw()

