from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = float(weight)
        self.started = False
        self.fuel = float(fuel)
        self.fuel_consumption = float(fuel_consumption)

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        if distance > 0:
            fuel_consumption = distance * self.fuel_consumption
            if fuel_consumption <= self.fuel:
                self.fuel -= fuel_consumption
            else:
                raise NotEnoughFuel