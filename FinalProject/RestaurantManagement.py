import csv

class Menu:
    def __init__(self):
        self.Items = []
        with open('FinalProject/items.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item_id = int(row['item_id'])  # Convert item_id to integer
                self.Items.append({
                    'item_id' : row['item_id'],
                    'item_name': row['item_name'],
                    'price': float(row['price'])  # Convert price to float
                })

    def AddItem(self):
        self.Items.append(
            {
            'item_id' : int(self.Items[-1]['item_id']) + 1,
            'item_name' : input("New Item name: "),
            'price' : input("New Item Price: ")
            }
        )
        with open('FinalProject/items.csv', 'w', newline='') as csvfile:
            fieldnames = ['item_id', 'item_name', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()  # Write the header row
            for item in self.Items:
                writer.writerow(item)
         
    def viewItems(self):
        print("Available Items on menu: ")
        print('No       Name                Price')
        for item in self.Items:
            print(f"{item['item_id']}       {item['item_name']} {' '*(20- len(item['item_name']))}{item['price']}$")

    def order(self):
        self.order = []
        name = False
        while name != 'exit': 
            name = input("Add Item to cart: ")
            quantity = int(input("Quantity: "))
            

choice = False
while choice != "exit":
    choice = input("Your Choice(show menu, add item, order, exit): ")
    newmenu = Menu()
    if choice == "show menu":
        newmenu.viewItems()
    if choice == "add item":
        newmenu.AddItem()
    if choice == "order":
        newmenu.viewItems()
        newmenu.order()