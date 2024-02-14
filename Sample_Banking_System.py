import random
import datetime
import pytz
import time
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance - amount < 0:
            print(currenttime.strftime("%B %d %Y (%A)"), currenttime.strftime("%I: %M: %S %p"))
            print("Transaction Failed: Not Enough Funds.")
        else:
            print(currenttime.strftime("%B %d %Y (%A)"), currenttime.strftime("%I: %M: %S %p"))
            print(f"Withdrawal of ${amount:.2f} successful.")
            self.balance -= amount
            print (f"Current Balance: ${self.get_balance()}\n")
    def get_balance(self):
        return format(self.balance,".2f")
    def display_info(self):
        print(currenttime.strftime("%B %d %Y (%A)"), currenttime.strftime("%I: %M: %S %p"))
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.get_balance()}")


currenttime = datetime.datetime.now(pytz.timezone("Asia/Manila"))
print(currenttime.strftime("%B %d %Y (%A)"), currenttime.strftime("%I: %M: %S %p"))
bankAccs = {

}
while True:
    type_of_user = input("Log in or Sign up? ").lower()
    if type_of_user == "log in" or type_of_user == "login":
        account_id = input("Please type your account ID: ")
        if account_id in list(bankAccs.keys()):
            print(f"Welcome {bankAccs[account_id].account_holder}!")
            while True:
                print("**- Deposit, Withdraw, Balance, Exit -**")
                activity = input("What activity would you like to do for today? ").lower()
                if "deposit" in activity:
                    while True:
                        try:
                            amount = int(input("Enter the amount you want to deposit: "))
                            bankAccs[account_id].deposit(amount)
                            print(currenttime.strftime("%B %d %Y (%A)"), currenttime.strftime("%I: %M: %S %p"))
                            print(f"${amount} is successfully added to your balance.\n")
                            break
                        except:
                            print("Invalid input. Please only enter a valid amount.")
                            continue
                elif "withdraw" in activity:
                    while True:
                        try:
                            amount = int(input("Enter the amount you want to withdraw: "))
                            if bankAccs[account_id].balance - amount < 0:
                                print("Transaction failed. Going back to main menu.")
                                break
                            else:
                                bankAccs[account_id].withdraw(amount)
                                break
                        except:
                            print("Invalid input. Please only enter a valid amount.")
                            continue
                elif "balance" in activity:
                    bankAccs[account_id].display_info()
                    continue
                elif "quit" in activity or "exit" in activity:
                    break
                else:
                    print("Invalid input. Please choose only between deposit, withdraw or exit/quit.")
        else:
            print("Account not found")
    elif type_of_user == "signup" or type_of_user == "sign up":
        account_name = input("Please enter your name: ")
        account_no = random.randint(1,99999)
        while True:
            for num in range(len(bankAccs)):
                if account_no in list(bankAccs.keys())[num]:
                    account_no = random.randint(1,99999)
            else:
                break
        bankAccs[f"{account_no}_{account_name}"] = BankAccount(account_no,account_name)
        print(f"Your account id will be: {account_no}_{account_name}")
        print("Please Remember it.\n")
    elif "quit" in type_of_user or "exit" in type_of_user:
        print("Thank you for using our program! Terminating...")
        time.sleep(2)
        break
else:
    print("Invalid input, Please Try Again.")