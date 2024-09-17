# Products available in the store by category  
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15),
        ("NVIDIA GPU", 1000)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450),
        ("Gaming Screens", 700),
        ("Sweeping Robot", 100),
        ("E-book Reader", 100)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8),
        ("Lays Chips", 6)
    ]
}

# Display categories
def display_categories():
    print("\nAvailable categories:")
    for i, category in enumerate(products.keys(), start=1):
        print(f"{i}. {category}")
    
    while True:
        category_choice = input("Enter the category number you want to explore: ")
        if category_choice.isdigit():
            category_index = int(category_choice) - 1
            if category_index in range(len(products)):
                return category_index
        print("Invalid input. Please enter a valid category number.")
        return None

# Display products in a selected category
def display_products(products_list):
    print("\nProducts available:")
    for i, (product, price) in enumerate(products_list, start=1):
        print(f"{i}. {product} - ${price}")

# Sort and display products based on price
def display_sorted_products(products_list, sort_order):
    reverse_order = (sort_order == 'desc')
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=reverse_order)
    display_products(sorted_products)
    return sorted_products

# Add selected products to the shopping cart
def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

# Display the contents of the shopping cart
def display_cart(cart):
    total_cost = sum(price * quantity for _, price, quantity in cart)
    print("\nShopping Cart:")
    for product, price, quantity in cart:
        print(f"{product} - ${price} x {quantity} = ${price * quantity}")
    print(f"Total cost: ${total_cost}")
    return total_cost

# Generate and display a receipt for the user
def generate_receipt(name, email, cart, total_cost, address):
    print(f"\nReceipt for {name} ({email}):")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

# Validate user name to contain first and last name, only alphabets
def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

# Validate email to contain an @ symbol
def validate_email(email):
    return "@" in email

# Main function where program starts
def main():
    name = input("Enter your name (first and last): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid first and last name.")
        name = input("Enter your name (first and last): ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email address: ")

    cart = []

    while True:
        category_index = display_categories()
        if category_index is None:
            continue
        selected_category = list(products.keys())[category_index]
        display_products(products[selected_category])
        
        while True:
            display_products(products[selected_category])
            user_choice = input("\nEnter an option: \n1. Select a product to buy\n2. Sort the products by price\n3. Go back to category selection\n4. Finish shopping\n")
            if user_choice == '1':
                product_choice = input("Enter the product number: ")
                if product_choice.isdigit() and 1 <= int(product_choice) <= len(products[selected_category]):
                    selected_product = products[selected_category][int(product_choice) - 1]
                    quantity = input("Enter the quantity: ")
                    if quantity.isdigit() and int(quantity) > 0:
                        add_to_cart(cart, selected_product, int(quantity))
                        print(f"Added {selected_product[0]} x {quantity} to the cart.")
                    else:
                        print("Invalid quantity.")
                else:
                    print("Invalid product number.")
            elif user_choice == '2':
                sort_order = input("Sort by price: \n1. Ascending\n2. Descending\n")
                sort_order_str = 'asc' if sort_order == '1' else 'desc'
                display_sorted_products(products[selected_category], sort_order_str)
            elif user_choice == '3':
                break  # Go back to category selection
            elif user_choice == '4':
                if cart:
                    total_cost = display_cart(cart)
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something next time.")
                return
            else:
                print("Invalid option. Please try again.")

# Make sure the main function runs when this script is executed
if __name__ == "__main__":
    main()
