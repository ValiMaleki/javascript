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
        elif new_speed <= 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list

    def hour_passes(self):
        for raceCar in cars_list:
            raceCar.acceleration(random.randint(-10, 15))
            raceCar.drive(1)

    def print_status(self):
        for raceCar in cars_list:
            print(f"{raceCar.registration_number:6s}  current speed: {raceCar.maximum_speed} km/h, travelled dictance {raceCar.travelled_distance} km")

    def race_finished(self):
        travMax = 0
        for car in self.car_list:
            travMax = max(car.travelled_distance, travMax)
        if travMax >= self.kilometers:
            return True




cars_list = []

for i in range(10):
    cars_list.append(Car(f'abc-{i}', random.randint(100, 200)))

race = Race('Grand Demolition Derby', 8000, cars_list)
print()

hour = 0
while race.race_finished() is not True:
    hour +=1
    race.hour_passes()
    if hour % 10 == 0:
        print(f'After {hour} hours:')
        race.print_status()
        print()
print(f'The race finished after {hour} hours:')
race.print_status()