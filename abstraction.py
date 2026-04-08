from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass


# Dog class
class Dog(Animal):
    def sound(self):
        print("Dog barks 🐶")


# Cat class
class Cat(Animal):
    def sound(self):
        print("Cat meows 🐱")


# ✅ User Input
if __name__ == "__main__":
    
    choice = input("Enter animal (dog/cat): ").lower()
    
    if choice == "dog":
        animal = Dog()
    elif choice == "cat":
        animal = Cat()
    else:
        print("Invalid choice")
        exit()
    
    animal.sound()