# """
# 🚀 QuickPedal Challenge: Rider Delivery Eligibility

# 📝 Task
# Write a function check_rider_eligibility(name, fuel_level, balance) that:

# Validates inputs

# name must be a non-empty string.

# fuel_level must be a number between 0 and 100.

# balance must be a number (int/float).

# Uses control flow (if, elif, else) and try…except

# If fuel_level < 20 → return "⚠️ Low fuel – rider cannot take deliveries."

# If balance < 100 → return "❌ Insufficient balance – rider must top up."

# If all checks pass → return "✅ Rider is eligible for deliveries."

# Handles errors gracefully with try … except.

# Example: if fuel_level = "abc" → show "❌ Error: Fuel level must be a number."
# """
# def check_rider_eligibility(name, fuel_level, balance):
#     try:
#         # Validate name
#         if not isinstance(name, str) or not name.strip():
#             raise ValueError("Name must be a non-empty string.")

#         # Validate fuel level
#         if not isinstance(fuel_level, (int, float)):
#             raise TypeError("Fuel level must be a number.")
#         if fuel_level < 0 or fuel_level > 100:
#             raise ValueError("Fuel level must be between 0 and 100.")

#         # Validate balance
#         if not isinstance(balance, (int, float)):
#             raise TypeError("Balance must be a number.")
#         if balance < 0:
#             raise ValueError("Balance cannot be negative.")

#         # QuickPedal rules
#         if fuel_level < 20:
#             return "Low fuel – rider cannot take deliveries."
#         elif balance < 100:
#             return "Insufficient balance – rider must top up."
#         else:
#             return " Rider is eligible for deliveries."

#     except (TypeError, ValueError) as e:
#         return f"Error: {e}"

# name = input("What is your name? ")
# favourite_color = input("What is your favourite color? ")
# print(name + " likes "+ favourite_color)


name = 51

if name < 3:
    print("name must be at least 3 characters")
elif name > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")