print("Welcome to Honey Buns Inventory Tracker!")
print("Let's keep track of our ingredients.")

inventory = {
    "eggs": 30,
    "cheese": 20,
    "bacon": 15,
    "sausage": 15,
    "chicken": 20,
    "potatoes": 25,
}

minimum_stock = {
    "eggs": 10,
    "cheese": 10,
    "bacon": 10,
    "sausage": 10,
    "chicken": 10,
    "potatoes": 10,
    "milk": 10,
}

def update_inventory(ingredient, amount):
    if ingredient in inventory:
        inventory[ingredient] = inventory[ingredient] + amount
    else:
        inventory[ingredient] = amount

def remove_inventory(ingredient, amount):
    if ingredient in inventory:
        if inventory[ingredient] >= amount:
            inventory[ingredient] = inventory[ingredient] - amount
        else:
            print(f"Not enough {ingredient} in inventory!")
    else:
        print(f"{ingredient.title()} is not in the inventory.")

def check_low_stock():
    print("\n--- LOW STOCK ALERTS ---")

    for ingredient, quantity in inventory.items():
        if quantity < minimum_stock[ingredient]:
            print(f"{ingredient.title()} needs restocking!")

# Update inventory
update_inventory("eggs", 10)
update_inventory("cheese", 5)
update_inventory("milk", 10)

# Remove inventory
remove_inventory("eggs", 5)
remove_inventory("cheese", 2)
remove_inventory("milk", 15)
remove_inventory("bacon", 10)

# Check for low stock
check_low_stock()

# Display inventory
print("\n--- HONEY BUNS INVENTORY ---")

for ingredient, quantity in inventory.items():
    print(f"{ingredient.title()}: {quantity}")