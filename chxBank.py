'''
1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.
'''
from py_compile import main

class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 2000

    def __str__(self):
        return f"BankAccount(username={self.username}, balance={self.balance})"

    def users_db(self, file_path):
        users = {}
        with open(file_path, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                users[username] = password
        return users

    def enter_credentials(self, username, password):
        if username in self.users_db("users_db.txt") and self.users_db("users_db.txt")[username] == password:
            return True
        else:
            return False

    def login(self):
        attempts = 0        
        while attempts < 3:
            print("Welcome to chxBanking System!")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.username = username
            self.password = password
            if self.enter_credentials(username, password):
                attempts = 0
                print("Login successful!")
                result = self.display_menu()
                print(result)
            else:
                attempts += 1
                print(f"Invalid credentials. Attempt {attempts} of 3.")
                


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0 and amount <=self.balance:
            self.balance -= amount
            return f"withdraw ${amount}. New balance:${self.balance}."
        elif amount > self.balance:
            return "Insuficient funds."
        else:
            return "Withdraw amount must be positive."
        
    def view_balance(self):
        return f"Current balance: ${self.balance}."

    def transfer(self, amount, recipient_account):
        if amount >0 and amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            return f"{amount} transfered to {recipient_account.username}. New balance: ${self.balance}."
        elif amount > self.balance:
            return "Insuficient balance."
        else:
            return "Transfer amount must be positive."

    def display_menu(self):
        choice =0
        choice = input("Welcome to chxBanking System menu \nPlease select your option: \n1. Deposit\n2. Withdraw\n3. View Balance\n4. Transfer\n5. Exit\n")
        if choice == '1. Deposit' or choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            choice = 1
            return self.perform_transaction(int (choice), amount=amount)
        elif choice == '2. Withdraw' or choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            choice = 2
            return self.perform_transaction(int(choice), amount=amount)
        elif choice == '3. View Balance' or choice == '3':
            choice = 3
            return self.perform_transaction(int(choice))
        elif choice == '4. Transfer' or choice == '4':
            amount = float (input('Enter the amount to transfer: '))
            recipient_username = input ("Enter the recipient's username: ")
            recipient_account = BankAccount(recipient_username, "password")
            choice = 4
            return self.perform_transaction(int(choice), amount=amount, recipient_account=recipient_account)
        elif choice == '5. Exit' or choice == '5':
            choice = 5
            return self.perform_transaction(int(choice))
        else:
            return "Invalid choice. Please try again."

    def perform_transaction(self, choice, amount=None, recipient_account=None):
        match choice:
            case 1:
                return self.deposit(amount)
            case 2:
                return self.withdraw(amount)
            case 3:
                return self.view_balance()
            case 4:
                return self.transfer(amount, recipient_account)
            case 5:
                print('Are you sure you want to exit? (yes/no)')
                if input().lower() == 'yes':
                    return "Exiting the system."
                else:
                    return self.display_menu()
main()

username = ""
password = ""
account = BankAccount(username, password)
account.login()

'''while attempts <= 3:
    if account.enter_credentials(username, password)== True:
        print("Login successful!")
        attempts = 0
        while True:
            result = account.display_menu()
            print(result)
            if result == "Exiting the system.":
                print("Thank you for using chxBanking System. Goodbye!")
                break            
        
    elif account.enter_credentials(username, password) == False and attempts < 3:
        attempts += 1
        print(f"Invalid credentials. Attempt {attempts} of 3.")
        result = account.display_menu()
        print(result)
        
        
    elif attempts == 3:
        print("Too many failed attempts. You are locked out.")
        break
    




*To run the code, simply execute this command "python chxBank.py users_db.txt" in your terminal. 
*Then follow the prompts to log in and perform transactions acording to users_db.txt data.
'''