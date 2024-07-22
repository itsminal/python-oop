class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def a(self):
        print("hi")


c1 = Customer("Nitish", 21)
c2 = Customer("Ankit", 21)
c3 = Customer("Neha", 21)

L = [c1, c2, c3]

for i in L:
    i.a()
