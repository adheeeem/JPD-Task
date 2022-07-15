import sys

class Products:
    product_list = []

    # Constructor
    def __init__(self, filename):
        self.filename = filename

        file = open(self.filename)
        self.product_list = list(map(lambda x: x.strip(), file.readlines()))
        file.close()

    # Method to show all the list items
    def show_list(self):
        cnt = 0
        for i in self.product_list:
            print(cnt, i.strip())
            cnt += 1
    
    # Method to edit the item
    def edit_item(self, ind, product, price):
        file = open(self.filename, 'w')
        item = product + ' - ' + str(price)
        self.product_list[ind] = item
        for i in range(len(self.product_list)):
            self.product_list[i] = self.product_list[i]+'\n'
        file.writelines(self.product_list)
        file.close()

    # Method to add a new item
    def add_item(self, product, price):
        file = open(self.filename, 'w')
        item = product + ' - ' + str(price)
        self.product_list.append(item)
        for i in range(len(self.product_list)):
            self.product_list[i] = self.product_list[i]+'\n'
        file.writelines(self.product_list)
        file.close()

    # Method to delete the item
    def delete_item(self, ind):
        self.product_list = [
            self.product_list[i]+'\n' for i in range(len(self.product_list)) if i != ind]
        file = open(self.filename, 'w')
        file.writelines(self.product_list)
        file.close()

    # Method to calculate the total price
    def calc(self):
        total_price = 0
        for item in self.product_list:
            dash = item.index('-')
            total_price += float(item[dash+1:].strip())
        return total_price

# Error handler for misspelled file name
try:
    if len(sys.argv) != 3: print("Missing some command line arguments")
    else:
        is_calc = False

        # Creating the object of the class Product
        products = Products(sys.argv[1])
        products.show_list()
        if sys.argv[2] == 'add':
            is_calc = True
            product = input("New product name: ")
            price = float(input("New product price: "))
            products.add_item(product, price)
        elif sys.argv[2] == 'edit':
            is_calc = True
            ind = int(input("Input the row index you want to edit: "))
            product = input(f"New product name for row {ind}: ")
            price = float(input(f"New product price for row {ind}: "))
            products.edit_item(ind, product, price)
        elif sys.argv[2] == 'delete':
            is_calc = True
            ind = int(input("Input the index of the product you want to delete: "))
            products.delete_item(ind)
        elif sys.argv[2] == 'calc':
            print('-' * 15)
            print("Total price:", products.calc())
        if is_calc:
            print("\nProducts list updated successfully")
            products.show_list()
except FileNotFoundError:
    print("File not found")