class fruit:
    list_fruitname = []
    list_username = []
    list_fruitprice = []
    list_quantity = []
    list_origin = []
    list_id = []
    orders = []
    count = 0

    def __init__(self, UserName, FruitName, FruitPrice, Quantity, Origin):
        self.__UserName = UserName
        self.__FruitName = FruitName
        self.__FruitPrice = float(FruitPrice)
        fruit.count += 1
        self.__id = fruit.count
        self.__Quantity = int(Quantity)
        self.__Origin = Origin

    @property
    def username(self):
        return self.__UserName

    @username.setter
    def username(self, UserName):
        self.__UserName = UserName

    @property
    def fruitname(self):
        return self.__FruitName

    @fruitname.setter
    def fruitname(self, FruitName):
        self.__FruitName = FruitName

    @property
    def fruitprice(self):
        return self.__FruitPrice

    @fruitprice.setter
    def fruitprice(self, FruitPrice):
        self.__FruitPrice = FruitPrice

    @property
    def quantity(self):
        return self.__Quantity

    @quantity.setter
    def quantity(self, Quantity):
        self.__Quantity = Quantity

    @property
    def origin(self):
        return self.__Origin

    @origin.setter
    def origin(self, Origin):
        self.__Origin = Origin

    def add_fruit(self):
        fruit.list_fruitname.append(self.__FruitName)
        fruit.list_fruitprice.append(self.__FruitPrice)
        fruit.list_quantity.append(self.__Quantity)
        fruit.list_origin.append(self.__Origin)
        fruit.list_id.append(fruit.count)
        print("Fruit added successfully!")
        system = fruit_shop_system()
        system.continue_screen()


class fruit_shop_system:
    def main_screen(self):
        while True:
            print("\nFRUIT SHOP SYSTEM")
            print("1. Create Fruit")
            print("2. View orders")
            print("3. Shopping (for buyer)")
            print("4. Exit")
            user = input("Please choose (1-4): ")
            if user == "1":
                self.create_fruit()
            elif user == "2":
                self.view_orders()
            elif user == "3":
                self.shopping()
            elif user == "4":
                exit()
            else:
                print("Invalid choice.")

    def create_fruit(self):
        print("CREATE FRUIT")
        username = input("Enter your name: ")
        name = input("Enter the name of the fruit: ")
        price = input("Enter the price of the fruit: ")
        quantity = input("Enter the quantity of the fruit: ")
        origin = input("Enter the origin of the fruit: ")
        fruit_input = fruit(username, name, price, quantity, origin)
        fruit_input.add_fruit()

    def view_orders(self):
        if not fruit.orders:
            print("No orders yet.")
            return
        for order in fruit.orders:
            print(f"\nCustomer: {order['username']}")
            print("Product | Quantity | Price | Amount")
            total = 0
            for item in order['items']:
                amount = item['quantity'] * item['price']
                total += amount
                print(f"{item['name']} | {item['quantity']} | {item['price']}$ | {amount}$")
            print(f"Total: {total}$")

    def shopping(self):
        if not fruit.list_fruitname:
            print("No fruits available.")
            return

        cart = []
        while True:
            print("\nList of Fruits:")
            print("| Item | Fruit Name | Origin | Price | Quantity |")
            for i in range(len(fruit.list_fruitname)):
                print(f"{i + 1}. {fruit.list_fruitname[i]} | {fruit.list_origin[i]} | {fruit.list_fruitprice[i]}$ | {fruit.list_quantity[i]}")

            try:
                item = int(input("Select item number: ")) - 1
                if item < 0 or item >= len(fruit.list_fruitname):
                    print("Invalid item.")
                    continue
                print(f"You selected: {fruit.list_fruitname[item]}")
                qty = int(input("Please input quantity: "))
                if qty > fruit.list_quantity[item]:
                    print("Not enough stock.")
                    continue
                fruit.list_quantity[item] -= qty
                cart.append({
                    "name": fruit.list_fruitname[item],
                    "price": fruit.list_fruitprice[item],
                    "quantity": qty
                })
                choice = input("Do you want to order now (Y/N)? ").lower()
                if choice == 'y':
                    break
            except:
                print("Invalid input.")

        print("\nYour Order:")
        total = 0
        print("Product | Quantity | Price | Amount")
        for item in cart:
            amount = item['quantity'] * item['price']
            total += amount
            print(f"{item['name']} | {item['quantity']} | {item['price']}$ | {amount}$")
        print(f"Total: {total}$")
        username = input("Enter your name: ")
        fruit.orders.append({"username": username, "items": cart})
        print("Order placed successfully!")

    def continue_screen(self):
        user = input("Do you want to continue? \n1. Yes \n2. No\n")
        if user == "1":
            self.main_screen()
        else:
            print("Returning to main menu...")


if __name__ == "__main__":
    system = fruit_shop_system()
    system.main_screen()
