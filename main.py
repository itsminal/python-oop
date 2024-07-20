class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def createPin(self):
        self.pin = input("Enter your pin")
        print("Pin set")

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            dep_amt = int(input("Enter the amt."))
            self.balance = self.balance + dep_amt
            print("DEposit done")
        else:
            print("wrong pin")

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            with_amt = int(input("Enter the amt."))
            if self.balance > with_amt:
                self.balance = self.balance - with_amt
                print("Withdrawal done")
            else:
                print("amount exceeded")

        else:
            print("wrong pin")

    def check_bal(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("wrong pin")

    def menu(self):
        user_ip = input("""
            Hello, how'd you like to proceed?
            Enter
            1. Create pin
            2. Deposit
            3. Withdraw
            4. Check Balance
            5. Exit
        """)
        if user_ip == "1":
            self.createPin()
        elif user_ip == "2":
            self.deposit()
        elif user_ip == "3":
            self.withdraw()
        elif user_ip == "4":
            self.check_bal()
        else:
            print("Exit")


Atm1 = Atm()
