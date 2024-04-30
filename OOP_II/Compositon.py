# Define classes representing CPU, RAM, and HardDrive components
class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self, size) -> None:
        self.size = size

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

# Define a class representing a Computer, composed of CPU, RAM, and HardDrive components
class Computer:
    def __init__(self, cores, ram_size, hd_capacity) -> None:
        # Composition: 
            # - Computer has a CPU
            # - Computer has a RAM
            # - Computer has a HardDrive
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disc = HardDrive(hd_capacity)

# Create an instance of Computer representing a Mac with specific configurations
mac = Computer(8, 16, 512)
print(mac.cpu.cores)  # Output: 8
print(mac.ram.size)  # Output: 16
print(mac.hard_disc.capacity)  # Output: 512


# Note: Composition is a design principle in object-oriented programming where objects of one class are composed of objects of another class. It represents a 'has a' relationship between classes where as inheritance represents 'is a' relationship.
# In this code, the Computer class has a CPU, RAM, and HardDrive, representing a 'has a' relationship between the Computer and its components.
# Each component is initialized within the Computer class constructor, demonstrating the composition relationship.
