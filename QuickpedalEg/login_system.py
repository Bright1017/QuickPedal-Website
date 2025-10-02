"""
📝 QuickPedal Challenge: Rider Login Simulation
Task

Write a function rider_login(email, password) that:

Validates inputs

If email is empty → raise ValueError("Email is required").

If password is empty → raise ValueError("Password is required").

Checks login

If email == "rider@quickpedal.com" and password == "secure123" → print ✅ Login successful!

Otherwise → raise PermissionError("Invalid email or password").

Handles errors gracefully

Show the rider a friendly message:

"❌ Login failed. Please check your details."

Log the real error message into a file called login_errors.txt.
"""


# def rider_login(email, password):
#     try:
#         # Input validation
#         if email == "":
#             raise ValueError("Email is required")
#         elif password == "":
#             raise ValueError("Password is required")

#         # Login check
#         if email != "rider@quickpedal.com" or password != "secure123":
#             raise PermissionError("Invalid email or password")
        
#         # Success
#         print(f"Welcome {email}, you are now logged in!")
    
#     except Exception as e:
#         # Friendly user message
#         print("Login failed! Please check your details.")
        
#         # Developer log (behind the scenes)
#         with open("login_errors.txt", "a") as log_file:
#             log_file.write(f"Error for user {email}: {e}\n")

