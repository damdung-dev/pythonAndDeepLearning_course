class Fruit:
    def __init__(self, fruit_id, name, price, quantity, origin):
        self.__fruit_id = Fruit_id
        self.__name = Name
        self.__price = Price
        self.__quantity = Quantity
        self.__origin = origin
    @property
    def fruit_id(self):
        return self.__fruit_id
    @fruit_id.setter
    def fruit_id(self, Fruit_id):
        self.__fruit_id = Fruit_id
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, Name):
        self.__name = Name
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, Price):
        self.__price = Price
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, Quantity):
        self.__quantity = Quantity
    @property
    def origin(self):
        return self.__origin
    @origin.setter
    def origin(self, Origin):
        self.__origin = Origin

    def get_info(self):
        return f"{self.__fruit_id}. {self.__name} - {self.__origin} - ${self.__price}"

    def update_quantity(self, amount):
        if self.__quantity >= amount:
            self.__quantity -= amount
            return True
        return False

    def get_price(self):
        return self.__price


class FruitShop:
    def __init__(self):
        self.__fruits = []
        self.__orders = {}

    def create_fruit(self):
        while True:
            fruit_id = len(self.__fruits) + 1
            name = input("Enter fruit name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            origin = input("Enter origin: ")
            self.__fruits.append(Fruit(fruit_id, name, price, quantity, origin))
            choice = input("Do you want to continue? \n1. Yes    2. No: ")
            if choice == "2":
                break

    def view_orders(self):
        if not self.__orders:
            print("No orders yet.")
            return
        for customer, items in self.__orders.items():
            print(f"\nCustomer: {customer}")
            total = 0
            for fruit, quantity, price in items:
                amount = quantity * price
                total += amount
                print(f"Product |  Quantity  |  Price   |  Amount")
                print(f"{fruit} | {quantity} | ${price} | ${amount}")
            print(f"Total: ${total}")

    def shopping(self):
        if not self.__fruits:
            print("No fruits available.")
            return

        cart = []
        while True:
            print("\nList of Fruits:")
            for fruit in self.__fruits:
                print(fruit.get_info())

            item = int(input("Select item to buy (0 to finish): "))
            if item == 0:
                break

            quantity = int(input("Enter quantity: "))
            selected_fruit = self.__fruits[item - 1]

            if selected_fruit.update_quantity(quantity):
                cart.append((selected_fruit.get_info().split(" - ")[0], quantity, selected_fruit.get_price()))
            else:
                print("Insufficient stock.")

            choice = input("Do you want to continue? \n1. Yes    2. No: ")
            if choice == "2":
                break

        if cart:
            name = input("Enter your name: ")
            self.__orders[name] = cart
            print("\nOrder Summary:")
            total = 0
            for fruit, quantity, price in cart:
                amount = quantity * price
                total += amount
                print(f"{fruit} | {quantity} | ${price} | ${amount}")
            print(f"Total: ${total}")

    def main_menu(self):
        while True:
            print("\nFRUIT SHOP SYSTEM\n1. Create Fruit\n2. View Orders\n3. Shopping\n4. Exit")
            sel = input("Choose one of these  options, Ppleaseplease : ")
            if sel == "1":
                self.create_fruit()
            elif sel == "2":
                self.view_orders()
            elif sel == "3":
                self.shopping()
            elif sel == "4":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    shop = FruitShop()
    shop.main_menu()