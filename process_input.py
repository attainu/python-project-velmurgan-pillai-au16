#process_input.py
#!/usr/bin/env python
import fileinput
import sys

from parking_lot import Parking
from car import Car

parking_lot = Parking()


def process(command_params):
    command_with_params = command_params.strip().split(' ')
    # print(command_with_params)
    command = command_with_params[0]

    if command == 'make_parking_lot':
        assert len(command_with_params) == 2, "create_parking_lot needs no of slots as well"
        assert command_with_params[1].isdigit() is True, "param should be 'integer type'"
        parking_lot.make_parking_lot(int(command_with_params[1]))

    elif command == 'car_park':
        assert len(command_with_params) == 3, "park needs registration number and color as well"
        car = Car(command_with_params[1], command_with_params[2])
        parking_lot.car_park(car)

    elif command == 'car_exit':
        assert len(command_with_params) == 2, "leave needs slot number as well"
        assert command_with_params[1].isdigit() is True, "slot number should be 'integer type'"

        parking_lot.car_exit(int(command_with_params[1]))

    elif command == 'parking_status':
        parking_lot.parking_status()

    elif command == 'registered_car_numbers_with_given_color':
        assert len(command_with_params) == 2, "registration_numbers_for_cars_with_colour needs color as well"
        parking_lot.registered_car_numbers_with_given_color(command_with_params[1])

    elif command == 'solts_numbers_of_cars_with_given_color':
        assert len(command_with_params) == 2, "slot_numbers_for_cars_with_colour needs color as well"
        parking_lot.solts_numbers_of_cars_with_given_color(command_with_params[1])

    elif command == 'slot_no_of_registered_car':
        assert len(command_with_params) == 2, "slot_number_for_registration_number needs registration_number as well"
        parking_lot.slot_no_of_registered_car(command_with_params[1])

    elif command == 'exit':
        exit(0)
    else:
        return ("Wrong command entered")


if len(sys.argv) == 1:
    while True:
        line = input()
        process(line)

else:
    for line in fileinput.input():
        process(line)
