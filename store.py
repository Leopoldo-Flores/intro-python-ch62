from catalog import catalog # import your catalog list

# Global shopping cart list
cart = []

def print_header(text):
    print("------------------")
    print(text)
    print("------------------")

def print_menu():
    print("Menu")
    print(" 1. - View Catalog")
    print(" 2. - Search Product")
    print(" 3. - View Cart")
    # Add more features
    print(" Q. - Quit")

def print_catalog():
    print_header("- Our Catalog -")
    for prod in catalog:
        print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
    
    answer = input("Type ID to add (N to close): ")
    if answer.lower == "n": 
        return
    else:
        add_product_to_cart(answer)
    
def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod) # add product to the cart
            print(f'{prod["title"]} added to your cart.')
            break

        if not found:
            print("This item is not in our catalog")
        print("------------------------\n")
    

# def seach_product():
# User input promt them ("search text: ")
# searching by title of product
# print (f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
# choice- if they actually want the product
def search_products():
    text = input("Search text: ").lower()
    found = False
    for prod in catalog: 
        if text in prod["title"].lower():
            found = True
            print (f'Found: ID {prod["id"]} | {prod["title"]} | ${prod["price"]} |')
            choice = input("Do you want to add this item to your cart? (y/n)")
            if choice.lower() == "y":
                add_product_to_cart(prod["id"])
            break
    if not found: 
        print("Sorry, this item dosen't exist.")
    print("------------------------\n")


# def view_cart():
# if- check if things are not in cart p"empty cart"
# else- check for products in cart
# print (f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
def view_cart():
    print_header("Your Cart")
    if not cart:
        print("Your cart is empty.")
    else:
        for prod in cart:
            print (f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
        cart_total()
        print("------------------------\n")
    

# def cart_total()
# total = 0
# += prices
def cart_total():
    total = 0 
    for prod in cart:
        total += prod["price"]
    print(f"Total: ${total}")

# Clear your cart
# def clear_cart():



# MAIN PROGRAM LOOP
option = ""
while option != "q" and option != "Q":
    print_header("Welcome to Store xy")
    print_menu()

    option = input("Choose an option: ")

    if option == "1":
        #print("print catalog")
        print_catalog()
    elif option == "2":
        # print("search product")
        search_products()
    elif option == "3":
        # print("view cart")
        view_cart()
    # Add other features
    elif option == "q" or option == "Q":
        print("Good Bye!")
        break
    else:
        print("** ERROR: Invalid Option!")
        print("------------------------\n")
