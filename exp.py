class HotelMenu:
    def __init__(self):
        self.menu = {
            "Burger": 5.99,
            "Pizza": 8.99,
            "Pasta": 7.99,
            "Salad": 4.99,
            "Soda": 1.99,
            "Water": 0.99
        }
        self.order = []

    def show_menu(self):
        print("Hotel Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def take_order(self):
        while True:
            item = input("Enter the name of the item you want to order (type 'done' to finish): ")
            if item.lower() == 'done':
                break
            if item in self.menu:
                self.order.append(item)
                print(f"{item} added to your order.")
            else:
                print("Sorry, we don't have that item. Please choose from the menu.")

    def calculate_bill(self):
        total = sum(self.menu[item] for item in self.order)
        return total

    def show_bill(self):
        print("\nYour order:")
        for item in self.order:
            print(f"{item}: ${self.menu[item]:.2f}")
        total = self.calculate_bill()
        print(f"\nTotal bill: ${total:.2f}")

def main():
    hotel_menu = HotelMenu()
    hotel_menu.show_menu()
    hotel_menu.take_order()
    hotel_menu.show_bill()

if __name__ == "__main__":
    main()

