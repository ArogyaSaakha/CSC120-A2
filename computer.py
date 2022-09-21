class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # Import a few useful containers from the typing module

    
    def create_computer(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description = description 
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        
    def description(self):
        return self.description
    def processor_type(self):
        return self.processor_type
    def hard_drive_capacity(self):
        return hard_drive_capacity
    def memory(self):
        return self.memory
    def operating_system(self):
        return self.operating_system
    def year_made(self):
        return self.year_made
    def price(self):
        return self.price 
    
    
    
        