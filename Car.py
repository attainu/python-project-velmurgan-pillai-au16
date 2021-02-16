import heapq
from collections import defaultdict, OrderedDict

class Car:
    def __init__(self, registration_number, color):
        self.registration_number = registration_number
        self.color = color

    def showCarDetails(self):

        car_details = "Car [registration_number=" + self.registration_number + ", color=" + self.color + "]"

        return car_details