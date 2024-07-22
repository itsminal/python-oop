class Atm:
    __counter = 1

    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.s_no = Atm.__counter
        Atm.__counter = Atm.__counter + 1
        # self.menu()

    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Not allowed")

    def createPin(self):
        print(self.__pin)
        self.__pin = input("Enter your pin")
        print(self.__pin)
        print("Pin set")

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            dep_amt = int(input("Enter the amt."))
            self.__balance = self.__balance + dep_amt
            print("DEposit done")
        else:
            print("wrong pin")

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            with_amt = int(input("Enter the amt."))
            if self.__balance > with_amt:
                self.__balance = self.__balance - with_amt
                print("Withdrawal done")
            else:
                print("amount exceeded")

        else:
            print("wrong pin")

    def check_bal(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            print(self.__balance)
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
            exit(0)
