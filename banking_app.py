# Parent class
class User():
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print('User details')
        print('')
        print('User: ', self.name)
        print('Age: ', self.age)
        print('Gender: ', self.gender)




# Child class
class Bank(User):
    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender)
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount 
        print('Account balance has been updated: £', self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds. Available balance: £', self.balance)
        else:
            self.balance -= amount
            print('Account balance has been updated: £', self.balance)
        
    def view_balance(self):
        self.show_details()
        print('Account balance: £', self.balance)



user1 = Bank('Becky', 23, 'Female')
user1.show_details()
user1.deposit(600)
user1.deposit(400)
user1.withdraw(400)
user1.withdraw(1000)
user1.view_balance()