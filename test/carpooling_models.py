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
        return f"Driver ID: {self.driver_id}, Name: {self.name}, Age: {self.age}, Chatty: {self.chatty}, Punctuality: {self.punctuality}, Safety: {self.safety}, Friendliness: {self.friendliness}, Comfortability: {self.comfortability}, Vehicle ID: {self.vehicle_id}"

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
        return f"Passenger ID: {self.passenger_id}, Name: {self.name}, Age: {self.age}, Chatty: {self.chatty}, Punctuality: {self.punctuality}, Safety: {self.safety}, Friendliness: {self.friendliness}, Comfortability: {self.comfortability}"

class Vehicle:
    def __init__(self, vehicle_id, model, year, number_of_seats, owner_name, driver_id=None):
        self.vehicle_id = vehicle_id
        self.model = model
        self.year = year
        self.number_of_seats = number_of_seats
        self.owner_name = owner_name  # Name of the owner of the vehicle
        self.driver_id = driver_id  # ID of the driver associated with this vehicle

    def __str__(self):
        return f"Vehicle ID: {self.vehicle_id}, Model: {self.model}, Year: {self.year}, Number of Seats: {self.number_of_seats}, Owner Name: {self.owner_name}, Driver ID: {self.driver_id}"


class Trip:
    def __init__(self, trip_id, driver_id, passenger_ids, vehicle_id, start_location, end_location):
        self.trip_id = trip_id
        self.driver_id = driver_id
        self.passenger_ids = passenger_ids
        self.vehicle_id = vehicle_id
        self.start_location = start_location
        self.end_location = end_location

    def __str__(self):
        passenger_info = ", ".join([f"Passenger ID: {passenger_id}" for passenger_id in self.passenger_ids])
        return f"Trip ID: {self.trip_id}, Driver ID: {self.driver_id}, Passengers: {passenger_info}, Vehicle ID: {self.vehicle_id}, Start Location: {self.start_location}, End Location: {self.end_location}"
