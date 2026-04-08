class details:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Country: {self.country}")
        
    def update_age(self, new_age):
        self.age = new_age
        print(f"Age updated to: {self.age}")    
        
person1 = details("Alice", 30, "USA")
person1.display()
person1.update_age(31)
person1.display()              