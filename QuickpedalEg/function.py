"""
Task: Build a Mini Rider Tracker

Create a simple Python program that:

Defines a Rider class.

Allows each rider to make deliveries and earn money.

Displays their name, total earnings, and number of deliveries.
"""


class Sender:
    # This code allows a Quickpedal User to Fill out who wants to send a package to their customer.

    def create_order(self):

        print("== Create A Delivery Order ==")
        # This code is Talking User Order Details.
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
    

# # creating a Rider class 
# class Rider:
#     species = "Home sapiens"


#     def __init__(self,name,bike_model):
#         self.name = name
#         self.bike_model = bike_model
#         self.balance = 0
#         self.deliveries = 0

#     def deliver_request(self, destination, earning):

sender1 = Sender()
sender1.create_order()
