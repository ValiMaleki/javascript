class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def acceleration(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed <=0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed






new_car=Car('abc-123', 142)
print( f"Registration Number: {new_car.registration_number}\nMaximum Speed: {new_car.maximum_speed} km/h" \
               f"\nCurrent Speed: {new_car.current_speed} km/h\nTravelled Distance: {new_car.travelled_distance} km")


new_car.acceleration(30)
print(f"The current speed is {new_car.current_speed} km/h")
new_car.acceleration(70)
print(f"The current speed is {new_car.current_speed} km/h")
new_car.acceleration(50)
print(f"The current speed is {new_car.current_speed} km/h")
new_car.acceleration(-200)
print(f"The current speed is {new_car.current_speed} km/h")


"""new_car = Car('abc-123', 142)
new_car._str_()"""

