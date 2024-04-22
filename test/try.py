import unittest
from carpooling_models import Driver, Passenger, Vehicle, Trip  # Import your classes from your module

class TestDriver(unittest.TestCase):
    def test_driver_initialization(self):
        driver = Driver("John", 35, chatty=True, punctuality=True, safety=True, friendliness=True, comfortability=True)
        self.assertEqual(driver.name, "John")
        self.assertEqual(driver.age, 35)
        self.assertTrue(driver.chatty)
        self.assertTrue(driver.punctuality)
        self.assertTrue(driver.safety)
        self.assertTrue(driver.friendliness)
        self.assertTrue(driver.comfortability)

class TestPassenger(unittest.TestCase):
    def test_passenger_initialization(self):
        passenger = Passenger("Alice", 25, chatty=False, punctuality=True, safety=True, friendliness=True, comfortability=True)
        self.assertEqual(passenger.name, "Alice")
        self.assertEqual(passenger.age, 25)
        self.assertFalse(passenger.chatty)
        self.assertTrue(passenger.punctuality)
        self.assertTrue(passenger.safety)
        self.assertTrue(passenger.friendliness)
        self.assertTrue(passenger.comfortability)

class TestVehicle(unittest.TestCase):
    def test_vehicle_initialization(self):
        vehicle = Vehicle("Toyota", "Camry", 2020, number_of_seats=5)
        self.assertEqual(vehicle.make, "Toyota")
        self.assertEqual(vehicle.model, "Camry")
        self.assertEqual(vehicle.year, 2020)
        self.assertEqual(vehicle.number_of_seats, 5)

class TestTrip(unittest.TestCase):
    def test_trip_initialization(self):
        driver = Driver("John", 35)
        passenger1 = Passenger("Alice", 25)
        passenger2 = Passenger("Bob", 30)
        vehicle = Vehicle("Toyota", "Camry", 2020, number_of_seats=5)
        trip = Trip(driver, [passenger1, passenger2], vehicle, "City A", "City B")

        self.assertEqual(trip.driver.name, "John")
        self.assertEqual(len(trip.passengers), 2)
        self.assertEqual(trip.vehicle.make, "Toyota")
        self.assertEqual(trip.start_location, "City A")
        self.assertEqual(trip.end_location, "City B")

if __name__ == '__main__':
    unittest.main()
