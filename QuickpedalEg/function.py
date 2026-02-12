# """
# Task: Build a Mini Rider Tracker

# Create a simple Python program that:

# Defines a Rider class.

# Allows each rider to make deliveries and earn money.

# Displays their name, total earnings, and number of deliveries.
# """


class Sender:
    # This code allows a Sender to create an Order or Package they want to send to their customer.

    def create_order(self):

        print("== Create A Delivery Order ==")
        # This code is Taking User Order Details.
        self.name = input("Enter your name: ").lower()
        self.item = input("What are you sending today? ").lower()
        self.destination = input("Enter the destination you want this package to be sent: ").lower()

        return {
            "sender_name": self.name,
            "item": self.item,
            "destination": self.destination,
            "assigned": None,
            "status": "pending"
        }
    
class RiderWallet():
    def __init__(self, rider_name):
        self.rider_name = rider_name
        self.__balance = 0.00
        print(f"Welcome, {self.rider_name} and your balance is: {self.__balance:.2f} ")

    def add_earning(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.rider_name}, You Received {amount:.2f}. New Balance: N{self.__balance:.2f}")
        else:
            print("Invalid Deposit Amount!.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.rider_name}, You've made a withdrawal of: N{amount:.2f}. from your account!")
        else:
            print("Your Account Balance Is Low!.")

    def platform_deducton_fee(self, amount):
        if 0 < amount <= self.__balance:
            print(f"the platform fees of {amount:.2f}, has been deducted from your balance!.")


    def check_balance(self):
        return self.__balance

# creating a Rider class 
class Rider:
    # this code creates an instance of the rider
    def __init__(self,name,bike_model):
        self.name = name 
        self.bike_model = bike_model
        self.wallet = RiderWallet(self.name)
        self.deliveries = 0

    # this code allows Riders to sees the order, the Sender Created
    def review_order(self, order, earning):
        print(f"{self.name}, You have a new delivery order")
        print(f"Item: {order['item']}")
        print(f"Destination: {order['destination']}")
        print(f"Sender: {order['sender_name']}")

        # This code allows riders to make a choice to accept/decline the order after review
        response = input("Do you wish to accept this delivery? (yes/no): ").lower()

        if response == "yes":
            order["assigned_to"] = self.name
            order["status"] = "Accepted"

            self.wallet.add_earning(earning)
            self.deliveries += 1

            print(f"{self.name} accepted the delivery!")
            print(f"Earned N{earning}. Total deliveries: {self.deliveries}")

            # this code takes out the platform fee, when the order is assigned to a rider
            platform_fee = 500
            self.wallet.platform_deducton_fee(platform_fee)


            return True

        else:
            print(f"{self.name} declined this order")
            return False
        
    def request_withdrawal(self):
        print(f"{self.name}, withdrawal request portal:")
        current_balance = self.wallet.check_balance()
        if current_balance > 0:
            try:
                amount = float(input("Enter the amount you wish to withdraw: "))
                self.wallet.withdraw(amount)
            except ValueError:
                print("Invalid input, Enter a numeric number:")

        else:
            print("You have no funds to withdraw!")
    
sender1 = Sender()
order = sender1.create_order()

# Available Riders
riders = [
    Rider("Bright", "Yamaha Xpress"),
    Rider("Chika", "Honda Powerbike"),
    Rider("Okezie", "Suzuki")
]

# Offering order to Riders
accepted_rider = None

for rider in riders:
    accepted = rider.review_order(order, earning = 1500)
    if accepted:
        accepted_rider = rider
        break

if accepted_rider:
    print(f"Order assigned to {accepted_rider.name}")
    rider_withdraw = input(f"{accepted_rider.name}, do you wish to make a withdraw? (yes/no): ")
    if rider_withdraw == "yes":
        accepted_rider.request_withdrawal()
    else:
        print("You can pick your next order!")

else:
    print("No Rider accepted the order yet. it remains pending")