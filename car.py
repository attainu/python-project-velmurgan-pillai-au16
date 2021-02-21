class Car:
    def __init__(self, register_car_no, color):
        self.register_car_no = register_car_no
        self.color = color

    def showCarDetails(self):

        return "Car [register_car_no=" + self.register_car_no + ", color=" + self.color + "]"

         