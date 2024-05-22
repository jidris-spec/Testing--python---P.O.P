import math

class ShoppingCart:
    def __init__(self):
        self.shopping = {}

    def add_to_cart(self):
        item = input("Enter the product you want to buy: ")
        price = float(input("Please enter the price of the product: "))

        if item in self.shopping:
            self.shopping[item] += price
        else:
            self.shopping[item] = price
        print(f"{item} has been added to your shopping cart and it is worth {price}")

    def display(self):
        print("Here are all the goods you want to purchase:")
        if not self.shopping:
            print("Your shopping cart is empty.")
        else:
            for item, price in self.shopping.items():
                print(f"{item} is in your shopping cart and it is worth {price}")

    def remove(self):
        item = input("Enter the product you want to remove: ")
        if item in self.shopping:
            del self.shopping[item]
            print(f"{item} has been removed from your shopping cart.")
        else:
            print(f"{item} is not in your shopping cart.")
    

    def calculate(self):
        total = sum(self.shopping.values())
        print(f"The total sum of all the products is {total}")

    def promo(self, discount):
        for product_name, product_price in self.shopping.items():
            self.shopping[product_name] = product_price * (1 - discount/100) 
            # calculated_bonus =  product_price * (1 - discount/100)
        print(f"The discount of  {discount} has been applied ")
    def start(self):
        while True:
            print("\n1. Add to cart\n2. Display goods\n3. Remove from cart\n4. Calculate total price\n9. promo\n5. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_to_cart()
            elif choice == "2":
                self.display()
            elif choice == "3":
                self.remove()
            elif choice == "4":
                self.calculate()
            elif choice == "9":
                bonus = float(input("Enter dicount percentage: "))
                self.promo(discount = bonus)
            elif choice == "5":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Instantiate the ShoppingCart object and start the program
shopping_cart = ShoppingCart()
shopping_cart.start()