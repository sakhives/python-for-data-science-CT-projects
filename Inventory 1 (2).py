# inventory.py
# =======CLASS ========== #

# Initialize shoes class with parameters country, code, product, cost, quantity
# Define functions for each parameter for the purpose of searching
# Define __str__ that returns object as a string
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"
     
# Use try/finally in case the file does not open on user end
# Define read_shoes_data() that reads each line from the text file
# Append items onto empty list
# Cast each item into an object and append to object list
shoes_list = []

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # skip the first line
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoes_list.append(Shoe(country, code, product, float(cost), int(quantity)))
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

# Use try/finally in case the file does not open on user end
# Define capture_shoes() that gets input from user for new products

def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoes_list.append(Shoe(country, code, product, cost, quantity))


def view_all():
    for shoe in shoes_list:
        print(shoe)

# Use try/finally in case the file does not open on user end
# Define restock() that displays first 5 items with lowest stock, using sort()
# Get info for each product using get_() class methods
# Display using tabulate
# Get input for new stock quantity
# Write to file and close

def re_stock():
    lowest_qty_shoe = min(shoes_list, key=lambda x: x.quantity)
    print(f"Shoe with lowest quantity: {lowest_qty_shoe}")
    add_qty = int(input("Enter quantity to add: "))
    lowest_qty_shoe.quantity += add_qty
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoes_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

# Define search_shoe() that displays specific shoe
# Get info for product using get_() class methods
# Display in console
def search_shoe():
    code = input("Enter shoe code: ")
    for shoe in shoes_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found.")

# Define value_per_item() that displays value for specific shoe
# Get info for product using get_() class methods
# Display in console
def value_per_item():
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"Product: {shoe.product}, Value: {value}")

# Define highest_quantity() that displays highest quantity
# Set empty list for quantity values
# Append values to list
# Display in console, using max()
# Mark item on sale

def highest_qty():
    highest_qty_shoe = max(shoes_list, key=lambda x: x.quantity)
    print(f"Product with highest quantity: {highest_qty_shoe.product}")


def main():
    read_shoes_data()
    while True:
        print("\nMenu:")
        print("1. Capture shoes data")
        print("2. View all shoes")
        print("3. Re-stock shoes")
        print("4. Search for a shoe")
        print("5. Calculate value per item")
        print("6. Find product with highest quantity")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            capture_shoes()
        elif choice == "2":
            view_all()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    #end program