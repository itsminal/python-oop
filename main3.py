class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_prof(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_add(new_city, new_pin, new_state)


class Address:

    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_add(self, new_city, new_pin, new_state):
        self.new_city = new_city
        self.new_pin = new_pin
        self.new_state = new_state


add = Address("Pune", 246897, "MH")
cust = Customer("Neha", "Female", add)

cust.edit_prof("siya","gurgaon",765768,"haryana")
print(cust.address.pincode)
