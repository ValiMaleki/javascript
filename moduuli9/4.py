import random

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

    def drive(self,hours):
        self.travelled_distance += self.current_speed * hours

cars_list=[]

for i in range(10):
    cars_list.append(Car(f'abc-{i}', random.randint(100, 200)))

travMax = 0
while travMax < 10000:
    for raceCar in cars_list:
        raceCar.acceleration(random.randint(-10, 15))
        raceCar.drive(1)
        travMax = max(raceCar.travelled_distance, travMax)
for raceCar in cars_list:
    print(f"{raceCar.registration_number:6s} : {raceCar.maximum_speed} km/h, {raceCar.travelled_distance} km")
print(f"the winner was able to travel {travMax}")










"""
new_car=Car('abc-123', 142)
print( f"Registration Number: {new_car.registration_number}\nMaximum Speed: {new_car.maximum_speed} km/h" \
               f"\nCurrent Speed: {new_car.current_speed} km/h\nTravelled Distance: {new_car.travelled_distance} km")


new_car.acceleration(60)
new_car.drive(1.5)
print(f"Car's traveled distance is {new_car.travelled_distance} km.")
"""



