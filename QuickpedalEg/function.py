"""
Task: Build a Mini Rider Tracker

Create a simple Python program that:

Defines a Rider class.

Allows each rider to make deliveries and earn money.

Displays their name, total earnings, and number of deliveries.
"""


class Sender:
    # This code allows a Sender to create an Order or Package they want to send to their customer.

    def create_order(self):

        print("== Create A Delivery Order ==")
        # This code is Taking User Order Details.
        self.name = input("Enter your name: ")
        self.item = input("What are you sending today? ")
        self.destination = input("Enter the destination you want this package to be sent: ")

        return {
            "sender_name": self.name,
            "item": self.item,
            "destination": self.destination,
            "assigned": None,
            "status": "pending"
        }
    

# creating a Rider class 
class Rider:
    # this code creates an instance of the rider
    def __init__(self,name,bike_model):
        self.name = name 
        self.bike_model = bike_model
        self.balance = 0
        self.deliveries = 0

    # this code allows Riders to see the order the Sender Created
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
            self.balance += earning
            self.deliveries += 1

            print(f"{self.name} accepted the delivery!")
            print(f"Earned ${earning}. Total deliveries: {self.deliveries}")

        else:
            print(f"{self.name} declines this order")
            return False
        return True
sender1 = Sender()
order = sender1.create_order()

# Available Riders
riders = [
    Rider("Tunde", "Yamaha Xpress"),
    Rider("Chika", "Honda Powerbike"),
    Rider("Yusuf", "Suzuki")
]

# Offering order to Riders

for rider in riders:
    accepted = rider.review_order(order, earning = 1500)
    if accepted:
        break

if order["assigned_to"]:
    print(f"Order assigned to {order['assigned_to']}")
else:
    print("No Rider accepted the order yet. it remains pending")