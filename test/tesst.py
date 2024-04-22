import csv
import random
import string

class Driver:
    def __init__(self, driver_id, name, age, chatty=False, punctuality=False, safety=False, friendliness=False, comfortability=False, vehicle_id=None):
        self.driver_id = driver_id
        self.name = name
        self.age = age
        self.chatty = chatty
        self.punctuality = punctuality
        self.safety = safety
        self.friendliness = friendliness
        self.comfortability = comfortability
        self.vehicle_id = vehicle_id

    def __str__(self):
        return f"{self.driver_id},{self.name},{self.age},{self.chatty},{self.punctuality},{self.safety},{self.friendliness},{self.comfortability},{self.vehicle_id}"

class Passenger:
    def __init__(self, passenger_id, name, age, chatty=False, punctuality=False, safety=False, friendliness=False, comfortability=False):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.chatty = chatty
        self.punctuality = punctuality
        self.safety = safety
        self.friendliness = friendliness
        self.comfortability = comfortability

    def __str__(self):
        return f"{self.passenger_id},{self.name},{self.age},{self.chatty},{self.punctuality},{self.safety},{self.friendliness},{self.comfortability}"

class Vehicle:
    def __init__(self, vehicle_id, model, year, number_of_seats, owner_name, driver_id=None):
        self.vehicle_id = vehicle_id
        self.model = model
        self.year = year
        self.number_of_seats = number_of_seats
        self.owner_name = owner_name
        self.driver_id = driver_id

    def __str__(self):
        return f"{self.vehicle_id},{self.model},{self.year},{self.number_of_seats},{self.owner_name},{self.driver_id}"

class Trip:
    def __init__(self, trip_id, driver_id, passenger_ids, vehicle_id, start_location, end_location):
        self.trip_id = trip_id
        self.driver_id = driver_id
        self.passenger_ids = passenger_ids
        self.vehicle_id = vehicle_id
        self.start_location = start_location
        self.end_location = end_location

    def __str__(self):
        passenger_info = ','.join([str(passenger_id) for passenger_id in self.passenger_ids])
        return f"{self.trip_id},{self.driver_id},{passenger_info},{self.vehicle_id},{self.start_location},{self.end_location}"

def generate_data(num_drivers, num_passengers, num_vehicles, num_trips):
    drivers = []
    passengers = []
    vehicles = []
    trips = []

    for i in range(num_drivers):
        driver_id = i + 1
        name = ''.join(random.choices(string.ascii_uppercase, k=5))
        age = random.randint(20, 60)
        chatty = random.choice([True, False])
        punctuality = random.choice([True, False])
        safety = random.choice([True, False])
        friendliness = random.choice([True, False])
        comfortability = random.choice([True, False])
        drivers.append(Driver(driver_id, name, age, chatty, punctuality, safety, friendliness, comfortability))

    for i in range(num_passengers):
        passenger_id = i + 1
        name = ''.join(random.choices(string.ascii_uppercase, k=5))
        age = random.randint(20, 60)
        chatty = random.choice([True, False])
        punctuality = random.choice([True, False])
        safety = random.choice([True, False])
        friendliness = random.choice([True, False])
        comfortability = random.choice([True, False])
        passengers.append(Passenger(passenger_id, name, age, chatty, punctuality, safety, friendliness, comfortability))

    for i in range(num_vehicles):
        vehicle_id = i + 1
        model = ''.join(random.choices(string.ascii_uppercase, k=5))
        year = random.randint(2000, 2022)
        number_of_seats = random.randint(2, 6)
        owner_name = ''.join(random.choices(string.ascii_uppercase, k=5))
        vehicles.append(Vehicle(vehicle_id, model, year, number_of_seats, owner_name))

    for i in range(num_trips):
        trip_id = i + 1
        driver_id = random.randint(1, num_drivers)
        passenger_ids = random.sample(range(1, num_passengers + 1), random.randint(1, 3))
        vehicle_id = random.randint(1, num_vehicles)
        start_location = ''.join(random.choices(string.ascii_uppercase, k=5))
        end_location = ''.join(random.choices(string.ascii_uppercase, k=5))
        trips.append(Trip(trip_id, driver_id, passenger_ids, vehicle_id, start_location, end_location))

    return drivers, passengers, vehicles, trips

def write_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Data"])
        for item in data:
            writer.writerow([type(item).__name__, str(item)])

num_drivers = 10000
num_passengers = 15000
num_vehicles = 8000
num_trips = 20000

drivers, passengers, vehicles, trips = generate_data(num_drivers, num_passengers, num_vehicles, num_trips)

all_data = drivers + passengers + vehicles + trips
write_to_csv(all_data, 'all_data.csv')

print("CSV file generated successfully.")
