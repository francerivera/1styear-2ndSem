import random
import datetime
import pytz

class BankAccount:
    total_deposits = 0
    total_withdraws = 0
    
    def __init__(self, account_number, account_holder, balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        self.total_deposits += 1 
        return f"Your current balance is now: ${round(self.balance, 2)}"
        
    def withdraw(self, amount): 
        if amount > self.balance: 
            print(time_in_ph.strftime(format = "%B %d, %Y  |  %H:%M"))
            print("Insufficient funds | Balance available: $", self.balance)
        else:
            self.balance -= amount 
            self.total_withdraws += 1
            print(time_in_ph.strftime(format = "%B %d, %Y  |  %H:%M"))
            print(f"Withdrawal of {amount} successful. Current Balance: $", self.balance) 
    
    def get_balance(self):
        return format(self.balance, ".2f")
        
    def display_info(self):
        print(time_in_ph.strftime(format = "%B %d, %Y  |  %H:%M"))
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.get_balance()}")

bank_accs = {}

while True:
    ph_timezone = pytz.timezone('Asia/Manila')
    time_in_ph = datetime.datetime.now(ph_timezone)
    print(time_in_ph.strftime(format = "%B %d, %Y  |  %H:%M"))  
    print("Welcome to Rivera Bank")
    new_user = input("Would you like to register a new account?\nType 'Yes' to create your bank | 'No' if you already have an account: ")
    if new_user.lower() == 'yes':
        account_holder = input("Please enter your name: ")
        account_number = random.randint(1,9999)
        while account_number in bank_accs: 
            account_number = random.randint(1,9999)
        bank_accs[account_number] = BankAccount(account_number, account_holder) 
        print("Account Number:", account_number)
        print("Account Holder:", account_holder.title())  
    elif new_user.lower() == 'no':
        account_pass = int(input("Please type your account number: ")) 
        if account_pass in bank_accs:
            while True:
                process = input("Here are the lists of options:\n(1) Deposit\n(2) Withdraw\n(3) Balance\n(4) Exit\nPlease choose the number you want: ")
                if process == '1':
                    try:
                        amount = float(input("Enter the amount you want to deposit: ")) 
                        bank_accs[account_pass].deposit(amount)
                        print(time_in_ph.strftime(format = "%B %d, %Y  |  %H:%M"))
                        print(f"${amount} is successfully added to your balance.\n")
                        break
                    except ValueError:
                        print("Invalid input. Please only enter a valid amount.")
                        continue
                elif process == '2':
                    try:
                        amount = float(input("Enter the amount you want to withdraw: ")) 
                        bank_accs[account_pass].withdraw(amount)
                        break
                    except ValueError:
                        print("Invalid input. Please only enter a valid amount.")
                        continue
                elif process == '3':    
                    bank_accs[account_pass].display_info()
                    continue
                elif process == '4':
                    break
                else:
                    print("Invalid input. Please choose only the numbers in the options.")
        else:
            print("Account not found.")
    else:
        print("Invalid input. Please Try Again.")

    
    

        
        
        
        
