from ast import Lambda
import sys

class Products:
    product_list = []
    def __init__(self, filename, action):
        self.filename = filename
        self.action = action

        file = open(self.filename)
        self.product_list = list(map(lambda x: x.strip(), file.readlines()))
        file.close()
    
    def show_list(self):
        for i in self.product_list: print(i.strip())

    def edit_list(self, ind, item):
        file = open(self.filename, 'w')
        self.product_list[ind] = item
        for i in range(len(self.product_list)):
            self.product_list[i] = self.product_list[i]+'\n'
        file.writelines(self.product_list)
        file.close()

    def add_item(self, item):
        file = open(self.filename, 'w')
        self.product_list.append(item)
        for i in range(len(self.product_list)):
            self.product_list[i] = self.product_list[i]+'\n'
        file.writelines(self.product_list)
        file.close()

    def delete_item(self, ind):
        self.product_list = [self.product_list[i]+'\n' for i in range(len(self.product_list)) if i != ind]
        file = open(self.filename, 'w')
        file.writelines(self.product_list)
        file.close()

products = Products(sys.argv[1], sys.argv[2])
products.show_list()
if sys.argv[2] == 'add':
    item = input("New item name: ")
    products.add_item(item)
elif sys.argv[2] == 'edit':
    ind = int(input("Input the row index you want to edit: "))
    item = input(f"New value for row {ind}: ")
    products.edit_list(ind, item)
elif sys.argv[2] == 'delete':
    ind = int(input("Input the index of the product you want to delete: "))
    products.delete_item(ind)
products.show_list()
    
# reading the data


#writing the data
#print(product_list)
    

