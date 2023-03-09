class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor= bottom_floor
        self.top_floor = top_floor
        self.current_floor= bottom_floor




    def floor_up (self):
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






h = Elevator(0,7)
h.go_to_floor(8)
h.go_to_floor(5)
h.go_to_floor(0)