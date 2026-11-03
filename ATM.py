


class Account:
    def __init__(self,account_number,pin,balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def verify_pin(self,entered_pin):
        return self.pin == entered_pin

    def get_balance(self):
        return self.balance

    def withdraw(self,amount):
        if amount <= 0:
            return False, "Amount mut be possitive."
        if amount > self.balance:
            return False, "Insufficient balance."
        self.balance -= amount
        return True, f"Withdrawal succesful. New balance: {self.balance}"

    def deposite(self,amount):
        if amount <= 0:
            return False, "Amount must be possitive."
        self.balance += amount
        return True, f"Deposit succcessful. New balance {self.balance}"

class ATM:
    def __init__(self):
        #mutiple accounts dictionary
        self.accounts = {
            "12345": Account("12345", "1234", 5000),
            "67890": Account("67890", "5678", 3000),
            "11111": Account("11111", "9999", 10000)
        }
        self.current_account = None

    def login(self,account_number,pin):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.verify_pin(pin):
                self.current_account = account
                return True, "login successfull"
            else:
                return False, "Invalid pin"
        else:
            return False, "Account not found"

    def check_balance(self):
        if self.currentaccount:
            balance = self.currentaccount.get_balance()
            return f"Current balance: {balance}"
        return "No account logged in"

    def withdraw(self,amount):
        if self.current_account:
            success, message = self.current_account.withdraw(amount)
            return message
        return "No account logged in"

    def depoit(self,amount):
        if self.amount:
            success, message = self.current_account.deposit(amount)
            return message
        return "No account logged in"

    def logout(self):
        self.current_account = None
        return "Logged out successfully"

    def display_menu(self):
        print("\n=====ATM MENU=====")
        print("1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Logout")
        print("=====================")

    def main():
        atm = ATM()

        #login
        print("=====ATM LOGIN=====")
        account_num = input("Enter account number: ")
        pin = input("Enter PIN: ")

        success, message = atm.login(account_num, pin)

        if not success:
            print(f"Login failed: {message}")
            return

        print(message)

        #menu loop
        while True:
            atm.display_menu()
            choice =  input("Enter your choice (1-4): ")

            if choice  == "1":
                print(atm.check_balance())

            elif choice == "2":
                amount = int(input("Enter the withdraw ammount: "))
                print(atm.withdraw (amount))

            elif choice == "3":
                amount = int(input("Enter withdraw amount"))
                print(atm.deposit(amount))

            elif choice == "4":
                def logout():
                    ...

                print(atm,logout())
                break

            else:
                print("invalid choice! please try agin later.")

if __name__ == "__main__":
    def main():
        ...

    main()

            



              
