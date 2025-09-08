# For Data Types in Python
from pyscript import display

# String
restaurant_name = 'Golden Spoon'
owner_name = 'Jillian Grospe'

# Integer
year_established = 1999

# Float
popular_item_price = 249.99

# Boolean
has_delivery = True

# List
product_names = ['Triple Patty Burger', 'Seafood Pasta', 'Red Velvet Lava Cake']

# List (instead of dictionary for hours)
business_hours = ['Opening: 8:00 AM', 'Closing: 10:00 PM']

# List
menu_prices = [
    'Triple Patty Burger: 249.99 php',
    'Seafood Pasta: 299.99 php',
    'Red Velvet Lava Cake: 199.99 php',
    'Grilled Salmon: 399.99 php',
    'Caesar Salad: 159.99 php'
]

# List
common_allergen = ['Peanuts', 'Dairy', 'Shellfish']

# Float
tax_rate = 0.09

# --- Display Info ---
display(f"{restaurant_name}", target="Header")
display( f"Owner: {owner_name}", target="Owner_Name")
display(f"{year_established}", target="Year")

# --- Display Menu Items ---
display(f"{menu_prices[0]}", target="row1")
display(f"{menu_prices[1]}", target="row2")
display(f"{menu_prices[2]}", target="row3")
display(f"{menu_prices[3]}", target="row4")