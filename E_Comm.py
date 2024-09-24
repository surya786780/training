class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}: {self.description}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to the cart.")

    def remove_item(self, product):
        self.items.remove(product)
        print(f"Removed {product.name} from the cart.")

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.items:
                print(item)

class User:
    def __init__(self, username):
        self.username = username
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product):
        self.shopping_cart.add_item(product)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_item(product)

    def checkout(self):
        total = self.shopping_cart.calculate_total()
        print(f"Total amount: ${total:.2f}")
        self.shopping_cart.items.clear()
        print("Thank you for your purchase!")


product1 = Product("Laptop", 999.99, "High-performance laptop")
product2 = Product("Headphones", 199.99, "Noise-cancelling headphones")

user = User("Alice")
user.add_to_cart(product1)
user.add_to_cart(product2)
user.shopping_cart.view_cart()
user.checkout()
