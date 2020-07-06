from poscontroller import POSController
from administrator import Administrator
import datetime
# from datetime import date
from datetime import timedelta
import random
import os


class POSScreen:
    def __init__(self):
        self.control = POSController()
        self.admin = Administrator()
        self.now = datetime.datetime.now()
        self.stockingdate = self.now.date()
        self.ondiscount = False
        self.invoiceno = 1

    def __str__(self):
        pass

    def displayMainMenu(self):
        countertoexit = 0
        while True:
            print("\t\t\tMonash Fruit and Vegetable Store\n")
            print("Date : " + str(self.now.date()) + "\t\t\t\t\t\t\t\t\t\t\tLogged in as" + str(self.admin.admin_name) + "\n")
            print("1. Checkout & Print Receipt")
            print("2. Daily Report")
            print("3. Display Local Supplier Stock")
            print("4. Display Overseas Supplier Stock")
            print("5. Exit Program")
            choice = int(input("Choose Option : "))
            if choice == 1:
                self.displayProductList()

            elif choice == 2:
                self.displayReport()

            elif choice == 3:
                self.displayLocalInventory()

            elif choice == 4:
                self.displayOverseasInventory()

            elif choice == 5:
                print("Thanks for using our product")
                print("Exiting......")
                break

            else:
                countertoexit += 1
                if countertoexit < 3:
                    print("Wrong Input!!!!")
                    print("Please Try Again\n\n")
                    os.system('cls')
                else:
                    print("Attempts all Invalid!!!!")
                    print("Exiting Program")
                    break

    def listitems(self, itemtype):
        if itemtype == 1:
            print("\n\t\tAvailable Fruits\n")
            sno = 1
            while sno <= 10:
                print(str(sno) + ". " + self.control.product.databank.get("Fruit", {}).get(int(sno), {}).get("name"))
                sno += 1
        elif itemtype == 2:
            print("\n\t\tAvailable Vegetables\n")
            sno = 1
            while sno <= 10:
                print(str(sno) + ". " + self.control.product.databank.get("Vegetable", {}).get(int(sno), {}).get("name"))
                sno += 1

    def displayLocalInventory(self):
        print("\t\t\tMonash Fruit and Vegetable Store\n")
        print("\tLocal Supplier Stock\n")

    def displayOverseasInventory(self):
        print("\t\t\tMonash Fruit and Vegetable Store\n")
        print("\tOverseas Supplier Stock\n")

    def displayProductList(self):
        while True:
            print("1. Fruits")
            print("2. Vegetables")
            fruitorveg = int(input("Which would you like to add from : "))
            self.listitems(fruitorveg)
            itemnumber = int(input("Select item to add to cart : "))
            print("1. PrePacked")
            print("2. Weighted")
            packingtype = int(input("Choose Packing type : "))
            if packingtype == 1:
                print("1. 5 KG Bag")
                print("2. 10 KG Bag")
                quantity = int(input("Which bag? : "))
                print("Choose Supplier type : ")
                print("1. Local Supplier")
                print("2. International Supplier")
                suppliertype = int(input("Supplier Type : "))
                self.control.addProduct(itemnumber, fruitorveg, packingtype, quantity, suppliertype)
            elif packingtype == 2:
                weight = int(input("Please specify weight (in KG) : "))
                print("Choose Supplier type : ")
                print("1. Local Supplier")
                print("2. International Supplier")
                suppliertype = int(input("Supplier Type : "))
                self.control.addProduct(itemnumber, fruitorveg, packingtype, weight, suppliertype)
            print("1. Add More Items")
            print("2. Print Receipt")
            proceed = int(input("Choose to Proceed : "))
            if proceed == 1:
                # self.printReceipt()
                self.control.productlist.__str__()
                self.displayProductList()
            elif proceed == 2:
                # self.control.generateReceipt(itemname, qty, price, packingtype)
                self.invoiceno += 1
                break
            else:
                break

    def printReceipt(self):
        pass
        # self.control.generateReceipt()

    def displayReport(self):
        print("\t\t\tMonash Fruit and Vegetable Store\n")
        print("\tDaily Report\n")

    def updateDates(self):
        inventorycount = [100, 80, 90, 70, 110]
        listofsuppliers = self.control.product.suppliers
        item = 1
        for values in self.control.product.databank["Fruit"]:
            self.control.product.databank["Fruit"][item]["stockdate"] = self.stockingdate
            self.control.product.databank["Fruit"][item]["expirydate"] = self.stockingdate + timedelta(days=self.control.product.databank["Fruit"][item].get("shelflife"))
            self.control.product.databank["Fruit"][item]["localinventory"] = random.choice(inventorycount)
            self.control.product.databank["Fruit"][item]["internationalinventory"] = random.choice(inventorycount)
            self.control.product.databank["Fruit"][item]["supplier"] = random.choice(listofsuppliers)
            item += 1

        item = 1
        for values in self.control.product.databank["Vegetable"]:
            self.control.product.databank["Vegetable"][item]["stockdate"] = self.stockingdate
            self.control.product.databank["Vegetable"][item]["expirydate"] = self.stockingdate + timedelta(days=self.control.product.databank["Vegetable"][item].get("shelflife"))
            self.control.product.databank["Vegetable"][item]["localinventory"] = random.choice(inventorycount)
            self.control.product.databank["Vegetable"][item]["internationalinventory"] = random.choice(inventorycount)
            self.control.product.databank["Vegetable"][item]["supplier"] = random.choice(listofsuppliers)
            item += 1


def main():
    pos = POSScreen()
    pos.updateDates()
    # print(pos.control.product.databank)
    pos.displayMainMenu()


if __name__ == "__main__":
    main()
