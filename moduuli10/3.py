"""Extend the program again by adding a method fire_alarm that does not receive
 any parameters and moves all elevators to the bottom floor. Continue the main
  program by causing a fire alarm in your building.

"""


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f'the elevator goes up to the floor {self.current_floor}')

    def floor_down(self):
        self.current_floor -= 1
        print(f'the elevator goes down to the floor {self.current_floor}')

    def go_to_floor(self, floor):
        if floor >= self.bottom_floor and floor <= self.top_floor:
            while self.current_floor != floor:
                if floor > self.current_floor:
                    self.floor_up()
                else:
                    self.floor_down()
            print("You have reached floor ", floor)
        else:
            print("Invalid floor number")


class Building:
    def __init__(self, elevators, bottom_num, top_num):
        self.bottom_num = bottom_num
        self.top_num = top_num

        self.elevators = [Elevator(bottom_num, top_num) for i in range(elevators)]

    def run_elevator(self, elevator_number, destination):
        self.elevators[elevator_number].go_to_floor(destination)

    """Extend the program again by adding a method fire_alarm that does not receive
     any parameters and moves all elevators to the bottom floor. Continue the main
      program by causing a fire alarm in your building.

    """

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_num)
            print(f'Fire alarm! '
                  f'Elevator no. {self.elevators.index(elevator) + 1} is now at floor {elevator.current_floor}! \n')


# In the main program, write the statements for creating a new building and running the elevators of the building.

new_Building = Building(2, 0, 10)

new_Building.run_elevator(0, 5)
new_Building.run_elevator(1, 7)


new_Building.fire_alarm()
