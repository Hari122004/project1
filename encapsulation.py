class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Invalid withdrawal amount")
    
    def get_balance(self):
        return self.__balance


class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade
    
    @property
    def name(self):
        return self.__name
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Grade must be between 0 and 100")


# ✅ User Input Section
if __name__ == "__main__":
    
    # --- Bank Account ---
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    
    account = BankAccount(name, balance)
    
    deposit_amount = float(input("Enter amount to deposit: "))
    account.deposit(deposit_amount)
    
    withdraw_amount = float(input("Enter amount to withdraw: "))
    account.withdraw(withdraw_amount)
    
    print(f"Current balance: ₹{account.get_balance()}")
    
    print("\n--- Student Details ---")
    
    # --- Student ---
    student_name = input("Enter student name: ")
    student_grade = int(input("Enter student grade: "))
    
    student = Student(student_name, student_grade)
    
    print(f"Student: {student.name}, Grade: {student.grade}")
    
    new_grade = int(input("Enter new grade: "))
    student.grade = new_grade
    
    print(f"Updated grade: {student.grade}")