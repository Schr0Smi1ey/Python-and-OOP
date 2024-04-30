class Vehicle: # Serves as the Base class for Bus and Truck
    def __init__(self, name, price):
        self.name = name  # Assign the name of the vehicle
        self.price = price  # Assign the price of the vehicle
    
    def __repr__(self):
        return f'Vehicle is {self.name} and costs {self.price}'  # Return a string representation of the vehicle

class Bus(Vehicle): # Serves as the Base class for ACBus
    def __init__(self, name, price, seat, driver_name, superviser_name):
        super().__init__(name, price)  # Call the constructor of the Vehicle class
        self.seat = seat  # Assign the number of seats in the bus
        self.driver_name = driver_name  # Assign the name of the driver
        self.superviser_name = superviser_name  # Assign the name of the supervisor
    
    def __repr__(self):
        return super().__repr__() + f' and has {self.seat} seats and is driven by {self.driver_name} and supervised by {self.superviser_name}'  # Return a string representation of the bus

class Truck(Vehicle): # Serves as the Base class for MiniTruck
    def __init__(self, name, price, Max_Load, Driver_name):
        super().__init__(name, price)  # Call the constructor of the Vehicle class
        self.Driver_name = Driver_name  # Assign the name of the truck driver
        self.Max_Load = Max_Load  # Assign the maximum load capacity of the truck
    
    def __repr__(self):
        return super().__repr__() + f' and has a maximum load of {self.Max_Load} and is driven by {self.Driver_name}'  # Return a string representation of the truck

# Multi-Level inheritance
class MiniTruck(Truck):
    def __init__(self, name, price, Max_Load, Driver_name):
        super().__init__(name, price, Max_Load, Driver_name)  # Call the constructor of the Truck class

    def __repr__(self):
        return super().__repr__()  # Output the representation of the MiniTruck object

class ACBus(Bus):
    def __init__(self, name, price, seat, driver_name, superviser_name, Avg_temperature):
        super().__init__(name, price, seat, driver_name, superviser_name)  # Call the constructor of the Bus class
        self.Avg_temperature = Avg_temperature  # Assign the average temperature of the AC bus
    
    def __repr__(self):
        return super().__repr__() + f' and has an average temperature of {self.Avg_temperature}'  # Return a string representation of the AC bus

# Creating an object of MiniTruck
van = MiniTruck('Tata ace', 5000000, 1000, 'karim')
print(van)  # Output the representation of the MiniTruck object

# Creating an object of ACBus
my_bus = ACBus('Volvo', 15000000, 30, 'John', 'Smith', 25)
print(my_bus)  # Output the representation of the ACBus object

# Explanation:

# Multi-level inheritance in Python, where classes inherit attributes and behavior from their parent classes.
# In multi-level inheritance, a class serves as a superclass for another class, which in turn can serve as a superclass for yet another class.
# Here, the MiniTruck class inherits from the Truck class, which itself inherits from the Vehicle class.
# Similarly, the ACBus class inherits from the Bus class, which also inherits from the Vehicle class.
