class Fruit:
    def __init__(self, fruit_id, name, price, quantity, origin):
        self.fruit_id = fruit_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.origin = origin

    def __str__(self):
        return f"{self.fruit_id}. {self.name} ({self.origin}) - {self.price}$"


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, fruit, quantity):
        if quantity <= fruit.quantity:
            self.items.append((fruit, quantity))
            fruit.quantity -= quantity
        else:
            print("Not enough stock available!")

    def display_order(self):
        print(f"Customer: {self.customer_name}")
        total = 0
        for fruit, quantity in self.items:
            amount = fruit.price * quantity
            total += amount
            print(f"{fruit.name} | {quantity} | {fruit.price}$ | {amount}$")
        print(f"Total: {total}$\n")


class FruitShop:
    def __init__(self):
        self.fruits = []
        self.orders = []

    def create_fruit(self):
        fruit_id = len(self.fruits) + 1
        name = input("Enter fruit name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        origin = input("Enter origin: ")
        self.fruits.append(Fruit(fruit_id, name, price, quantity, origin))
        print("Fruit added successfully!\n")

    def view_orders(self):
        if not self.orders:
            print("No orders yet.\n")
            return
        for order in self.orders:
            order.display_order()

    def shop(self):
        if not self.fruits:
            print("No fruits available.\n")
            return

        print("Available Fruits:")
        for fruit in self.fruits:
            print(fruit)

        order = Order(input("Enter your name: "))
        while True:
            item_no = int(input("Select fruit number: ")) - 1
            if 0 <= item_no < len(self.fruits):
                quantity = int(input(f"Enter quantity for {self.fruits[item_no].name}: "))
                order.add_item(self.fruits[item_no], quantity)
            else:
                print("Invalid selection.")

            cont = input("Do you want to order more? (Y/N): ").upper()
            if cont == "N":
                break

        self.orders.append(order)
        print("Order placed successfully!\n")

    def run(self):
        while True:
            print("\nFRUIT SHOP SYSTEM")
            print("1. Create Fruit")
            print("2. View Orders")
            print("3. Shopping")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.create_fruit()
            elif choice == "2":
                self.view_orders()
            elif choice == "3":
                self.shop()
            elif choice == "4":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    shop = FruitShop()
    shop.run()