#Inventory Management
'''Problem Statement: Create a dictionary to maintain the stock of products in a shop.
Example:
{ 'Laptop': 15, 'Mouse': 40, 'Keyboard': 25, 'Monitor': 10 }
Implement the following:
•
Add a new product.
•
Update the stock of an existing product.
•
Remove a product from inventory.
•
Display products having stock less than 20.
•
Display the total number of items available in the inventory.'''
#--------------------------------coding-----------------------------------------------
# Initial inventory dictionary
inventory = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

# 1. Add a new product
inventory["Printer"] = 12
print("\nAfter adding a new product:")
print(inventory)

# 2. Update the stock of an existing product
inventory["Laptop"] = 20
print("\nAfter updating Laptop stock:")
print(inventory)

# 3. Remove a product from inventory
del inventory["Monitor"]
print("\nAfter removing Monitor:")
print(inventory)

# 4. Display products having stock less than 20
print("\nProducts with stock less than 20:")
for product, stock in inventory.items():
    if stock < 20:
        print(f"{product}: {stock}")

# 5. Display the total number of items available in the inventory
total_items = sum(inventory.values())
print(f"\nTotal items in inventory: {total_items}")
#--------------------------------------------------------------------------------------------------
'''output:
After adding a new product:
{'Laptop': 15, 'Mouse': 40, 'Keyboard': 25, 'Monitor': 10, 'Printer': 12}
After updating Laptop stock:
{'Laptop': 20, 'Mouse': 40, 'Keyboard': 25, 'Monitor': 10, 'Printer': 12}
After removing Monitor:
{'Laptop': 20, 'Mouse': 40, 'Keyboard': 25, 'Printer': 12}
Products with stock less than 20:
Laptop: 20
Keyboard: 25
Printer: 12

Total items in inventory: 97
'''