class JewelryApp:
    def __init__(self):
        self.inventory = {
            "rings": {"gold Rings": 200, "silver Ring": 100, "diamond Ring": 500},
            "necklaces": {"gold Necklace": 1000, "silver Necklace": 500, "Pearl Necklace": 800},
            "bracelets": {"Gold Bracelet": 300, "silver Bracelet": 150, "Diamond Bracelet": 700}
        }
        self.cart = {}
        def display_menu (self):
            print("Welcome to the Jewelry Store!")
            print("1. Browse Jewelry")
            print("2. Add to Cart")
            print("3. view cart")
            print("4. checkout")
            print("5. Exit")
        def browse_jewelry(self):
            print("Available Jewelry:")
            for category, items in self.inventory.items():
                print(f"{category}:")
                for item, price in items.items():
                    print(f"{item} - ${price}")
def add_to_cart(self):
    category = input("Enter a category (rings, necklaces, bracelets): ").capitalize()
    if category not in self.inventory:
        print("Invalid category")
        return
    item = input(f"Enter the item name from {category}: ")
    if item not in self.inventory[category]:
        print("Invalid item")
        return 

    quantity = int(input("Enter the quantity: "))
    if item in self.cart:
        self.cart[item] += quantity
    else:
        self.cart[item] = {
         'price': self.inventory[category][item],
            'quantity': quantity
        }
    print(f"{quantity} x {item} added to cart")
def view_cart(self):
    if not self.cart:
        print("Cart is empty")
        return
    print("Your Cart:")
    total = 0
    for item, details in self.cart.items():
        item_total = details['price'] * details['quantity']
        total += item_total
        print(f"{item} - ${details['price']} x {details['quantity']} = ${item_total}")
    print(f"Total: ${total}")
def checkout(self):
    if not self.cart:
        print("Cart is empty Add some items to checkout")
        return
    self.view_cart()
    print ("Thank you for shopping with us!")
    self.cart.clear()
def run(self):
    while True:
      self.display_menu()
      choice = input("Enter your choice: ")
      if choice == "1":
          self.browse_jewelry()
      elif choice == "2":
          self.add_to_cart()
      elif choice == "3":
          self.view_cart()
      elif choice == "4":
          self.checkout()
      elif choice == "5":
          print("Thank you for visiting the Jewelry Ordering App. Goodbye!")
          break
      else:
          print("Invalid choice")
if __name__ == "__main__":
    app = JewelryApp()
    app.run()
app.run()
