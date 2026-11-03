


class Bankaccount:
    def __init__(self,account_number,name,balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposite(self,amount):
        self.balance += amount
        print(f"Deposited {amount} New balance: {self.balance}\n")

    def withdraw(self,amount):
        if amount <= self.balance:
            print("Withdrawal amount must be possitive")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance:{self.balance}")

    def display_balance(self):
        print(f"account:{self.accpount_number}|name: {self.name}| balance: {self.balance}")

class Bank:
    def __iniy__(self):
        self.accounts = {}
        self.next_id = 1001

    def create_acount(self,name,initial_deposite):
        acc_num = self.next_id
        self.accounts[acc_num] = Bankaccount(acc_num,name,initial_deposite)
        self.next_id += 1
        print(f"Account created for {name}. Account number:{acc_num}")

    def search_account(self,account_number):
        account = self.accounts.get(account_number)
        if account is None:
            print("Account not found")
        return account

    def deposit(self,account_number,amount):
        account = self.search_account(account_number)
        if account:
            account.deposit(amount)

    def withdraw(self,account_number,amount):
        account = self.search_account(account_number)
        if account:
            account.withdraw(amount)

    def display_balance(self,account_number):
        account = self.search_account(account_number)
        if account:
            account.display_balance()

def main():
    bank = Bank()
    while True:
        print("\n1.Craete Account\n2.Deoposit\n3.Withdraw\n4.Display balance\n5.search account\n6.Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            amount = float(input("Enter initial deposit amount: "))
            bank.create_acount(name, amount)

        elif choice == "2":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter Deposit amount: "))
            bank.deposit(acc_num, amount)

        elif choice == "3":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(acc_num, amount)

        elif choice == "4":
            acc_num = int(input("Enter account number: "))
            bank.display_balance(acc_num)

        elif choice == "5":
            acc_num = int(input("Enter account number: "))
            account = bank.search_account(acc_num)
            if account:
                account.display_balance()

        elif choice == "6":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()




                



                                                      


              