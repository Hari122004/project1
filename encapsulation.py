class BankAccount:
    """Demonstrates encapsulation with private and public attributes."""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute
    
    def deposit(self, amount):
        """Public method to deposit money."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Public method to withdraw money."""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount")
    
    def get_balance(self):
        """Public method to access private balance."""
        return self.__balance
    
    def __calculate_interest(self, rate=0.02):
        """Private method - only accessible within the class."""
        return self.__balance * rate


class Student:
    """Another encapsulation example with property decorators."""
    
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade
    
    @property
    def name(self):
        """Property to get name."""
        return self.__name
    
    @property
    def grade(self):
        """Property to get grade."""
        return self.__grade
    
    @grade.setter
    def grade(self, new_grade):
        """Property setter with validation."""
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Grade must be between 0 and 100")


# Example usage
if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Current balance: ${account.get_balance()}")
    
    student = Student("Alice", 85)
    print(f"Student: {student.name}, Grade: {student.grade}")
    student.grade = 90
    print(f"Updated grade: {student.grade}")
