import heapq
from collections import defaultdict, OrderedDict

# class Car:
#     def __init__(self, register_car_no, color):
#         self.register_car_no = register_car_no
#         self.color = color

#     def showCarDetails(self):

#         return "Car [register_car_no=" + self.register_car_no + ", color=" + self.color + "]"

class Parking: 

    def __init__(self):
        self.register_car_no = dict()
        self.register_car_color = defaultdict(list)
        self.car_slot_no = OrderedDict()
        self.slot_available_to_park = []


    def make_parking_lot(self, total_slots):
        
        print("Created a parking lot with {} slots".format(total_slots))

        for i in range(1, total_slots + 1):
            heapq.heappush(self.slot_available_to_park, i)
        return True 


    def parking_status(self):
        print("Slot No.  Registration No  Colour")
        for slot, car in self.car_slot_no.items():
                print("{}         {}    {}".format(slot, car.register_car_no, car.color))
        return True

     
    def find_nearest_slot(self):
        
        return heapq.heappop(self.slot_available_to_park) if self.slot_available_to_park else None

    def car_exit(self, slot_to_freed):
        found = None
        for registration_no, slot in self.register_car_no.items():
            if slot == slot_to_freed:
                found = registration_no

        if found:
            heapq.heappush(self.slot_available_to_park, slot_to_freed)
            del self.register_car_no[found]

            car_to_leave = self.car_slot_no[slot_to_freed]
            self.register_car_color[car_to_leave.color].remove(found)
            del self.car_slot_no[slot_to_freed]

            print("Slot number {} is free".format(slot_to_freed))
            return True
            
        else:
            print("slot is not in use")
            return False

    def car_park(self, car):

        slot_no = self.find_nearest_slot()

        if slot_no is None:
            print("SORRY - Parking lot Is Full")
            return
        print("Slot Number Given is: {}".format(slot_no))

        self.car_slot_no[slot_no]  = car
        self.register_car_no[car.register_car_no] = slot_no
        self.register_car_color[car.color].append(car.register_car_no)
        return slot_no

    def registered_car_numbers_with_given_color(self, color):
        registration_numbers = self.register_car_color[color]
        print("' ".join(registration_numbers))
        return self.register_car_color[color]

    #   This function will tell all Slot numbers of car present 
    #   in the parking lot -> with given color

    def solts_numbers_of_cars_with_given_color(self, color):
        registration_numbers = self.register_car_color[color]
        slots = [self.register_car_no[reg_no] for reg_no in registration_numbers]
        print("' ".join(map(str, slots)))
        return slots

    #   This function will tell slot number of an registered car no.

    def slot_no_of_registered_car(self, registration_number):
        slot_number = None
        if registration_number in self.register_car_no:
            slot_number = self.register_car_no[registration_number]
            print(slot_number)
            return slot_number
        else:
            print("Not found")
            return slot_number
