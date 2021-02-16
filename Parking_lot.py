import heapq
from collections import defaultdict, OrderedDict

class Parking:

    def __init__(self):
        self.register_car_no = dict()
        self.register_car_color = defaultdict(list)
        self.car_slot_no = orderedDict()
        self.slot_available_to_park = []


    def make_parking_lot(self, total_slots):
        
        print("Created a parking lot with {} slots".format(total_slots))

        for i in range(1, total_slots + 1):
            heapq.heappush(self.slot_available_to_park, i)
        return True 
    
    def car_park(self):

        slot_no = self.find_nearest_slot()

        if slot_no is None:
            print("SORRY - Parking lot Is Full")
            return
        print("Slot Number Given is: {}".format(slot_no))

        self.car_slot_no[slot_no]  = car
        self.register_car_no[car.register_car_no] = slot_no
        self.register_car_color[car.color].append(car.register_car_no)
        return slot_no


    def find_nearest_slot(slef):
        return heapq.heappop(self.slot_available_to_park) if self.slot_available_to_park else None


    def car_exit(self, slot_to_freed):
        found = None
        for registration_no, slot in self.register_car_no.items():
            if slot == slot_to_freed:
                found = registration_no

"""
Now lets clean all the cache
"""
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


    def parking_status(self):
        print("Slot No.  Registration No  Colour")
        for slot, car in self.car_slot_no.items():
             print("{}         {}    {}".format(slot, car.registration_number, car.color))
        return True
