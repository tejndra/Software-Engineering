import datetime
from datetime import date
from datetime import timedelta
# from cart import Cart
import os


class Mfv:

    def __init__(self):
        self.cartquantity = 0
        self.databank = {
            "Fruit": {
                1:
                    {"name": "Apple",
                     "shelflife": 9,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                2:
                    {"name": "Banana",
                     "shelflife": 4,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                3:
                    {"name": "Blueberry",
                     "shelflife": 7,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                4:
                    {"name": "Cherry",
                     "shelflife": 4,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                5:
                    {"name": "Grapes",
                     "shelflife": 5,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                6:
                    {"name": "Orange",
                     "shelflife": 7,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                7:
                    {"name": "Pineapple",
                     "shelflife": 5,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                8:
                    {"name": "Pear",
                     "shelflife": 7,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                9:
                    {"name": "Strawberry",
                     "shelflife": 4,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                10:
                    {"name": "Watermelon",
                     "shelflife": 7,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     }
            },
            "Vegetable": {
                1:
                    {"name": "Beetroot",
                     "shelflife": 9,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                2:
                    {"name": "Cabbage",
                     "shelflife": 9,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                3:
                    {"name": "Carrot",
                     "shelflife": 9,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                4:
                    {"name": "Cauliflower",
                     "shelflife": 7,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                5:
                    {"name": "Corn",
                     "shelflife": 4,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                6:
                    {"name": "Cucumber",
                     "shelflife": 5,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                7:
                    {"name": "Onion",
                     "shelflife": 9,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                8:
                    {"name": "Potato",
                     "shelflife": 9,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                9:
                    {"name": "Spinach",
                     "shelflife": 7,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     },
                10:
                    {"name": "Tomato",
                     "shelflife": 7,
                     "supplier": None,
                     "price": 2,
                     "stockdate": None,
                     "expirydate": None
                     }
            }
        }
        self.cart = []
        self.now = datetime.datetime.now()
        self.stockingdate = self.now.date()
        self.todaysdate = date(2018, 9, 17)
        self.ondiscount = False
        self.invoiceno = 1

    def __str__(self):
        pass

    def listitems(self, itemtype):
        if itemtype == 1:
            print("\n\t\tAvailable Fruits\n")
            sno = 1
            while sno <= 10:
                print(str(sno) + ". " + self.databank.get("Fruit", {}).get(int(sno), {}).get("name"))
                sno += 1
        elif itemtype == 2:
            print("\n\t\tAvailable Vegetables\n")
            sno = 1
            while sno <= 10:
                print(str(sno) + ". " + self.databank.get("Vegetable", {}).get(int(sno), {}).get("name"))
                sno += 1

    def checkdiscount(self, expiringdate):
        delta = expiringdate - self.todaysdate
        if delta.days <= 3:
            print("Discount Applied")
        else:
            print("Original Price with GST")

    def invoicecalc(self, itemname, qty, price, packingtype):
        pass

    def additemtocart(self, itemno, itemtype, packtype, measure):
        counter = False
        if itemtype == 1:
            if packtype == 1 and measure == 1:
                if self.databank["Fruit"][itemno].get("prepacked5onshelf") == 0:
                    self.databank["Fruit"][itemno]["prepacked5onshelf"] = 8
                    self.databank["Fruit"][itemno]["prepacked5onshelf"] -= 1
                    self.checkdiscount(self.databank["Fruit"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)
                else:
                    self.databank["Fruit"][itemno]["prepacked5onshelf"] -= 1
                    self.checkdiscount(self.databank["Fruit"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)

            elif packtype == 1 and measure == 2:
                if self.databank["Fruit"][itemno].get("prepacked10onshelf") == 0:
                    self.databank["Fruit"][itemno]["prepacked10onshelf"] = 6
                    self.databank["Fruit"][itemno]["prepacked10onshelf"] -= 1
                    self.checkdiscount(self.databank["Fruit"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)
                else:
                    self.databank["Fruit"][itemno]["prepacked10onshelf"] -= 1
                    self.checkdiscount(self.databank["Fruit"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)

            elif packtype == 2:
                if self.databank["Fruit"][itemno].get("qtyonshelf") == 0:
                    self.databank["Fruit"][itemno]["qtyonshelf"] = 12
                    self.databank["Fruit"][itemno]["qtyonshelf"] -= measure
                    self.checkdiscount(self.databank["Fruit"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)
                else:
                    self.databank["Fruit"][itemno]["qtyonshelf"] -= measure
                    self.checkdiscount(self.databank["Fruit"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)

        elif itemtype == 2:
            if packtype == 1 and measure == 1:
                if self.databank["Vegetable"][itemno].get("prepacked5onshelf") == 0:
                    self.databank["Vegetable"][itemno]["prepacked5onshelf"] = 8
                    self.databank["Vegetable"][itemno]["prepacked5onshelf"] -= 1
                    self.checkdiscount(self.databank["Vegetable"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)
                else:
                    self.databank["Vegetable"][itemno]["prepacked5onshelf"] -= 1
                    self.checkdiscount(self.databank["Vegetable"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)

            elif packtype == 1 and measure == 2:
                if self.databank["Vegetable"][itemno].get("prepacked10onshelf") == 0:
                    self.databank["Vegetable"][itemno]["prepacked10onshelf"] = 6
                    self.databank["Vegetable"][itemno]["prepacked10onshelf"] -= 1
                    self.checkdiscount(self.databank["Vegetable"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)
                else:
                    self.databank["Vegetable"][itemno]["prepacked10onshelf"] -= 1
                    self.checkdiscount(self.databank["Vegetable"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)

            elif packtype == 2:
                if self.databank["Vegetable"][itemno].get("qtyonshelf") == 0:
                    self.databank["Vegetable"][itemno]["qtyonshelf"] = 12
                    self.databank["Vegetable"][itemno]["qtyonshelf"] -= measure
                    self.checkdiscount(self.databank["Vegetable"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)
                else:
                    self.databank["Vegetable"][itemno]["qtyonshelf"] -= measure
                    self.checkdiscount(self.databank["Vegetable"][itemno].get("expirydate"))
                    self.invoicecalc(self.databank["Fruit"][itemno].get("name"), measure, self.databank["Fruit"][itemno].get("price"), packtype)

    def updatedates(self):
        item = 1
        for values in self.databank["Fruit"]:
            self.databank["Fruit"][item]["stockdate"] = self.stockingdate
            self.databank["Fruit"][item]["expirydate"] = self.stockingdate + timedelta(days=self.databank["Fruit"][item].get("shelflife"))
            item += 1

        item = 1
        for values in self.databank["Vegetable"]:
            self.databank["Vegetable"][item]["stockdate"] = self.stockingdate
            self.databank["Vegetable"][item]["expirydate"] = self.stockingdate + timedelta(days=self.databank["Vegetable"][item].get("shelflife"))
            item += 1

    def printreceipt(self):
        print("\t\t\tMonash Fruit and Vegetable Store\n")
        print("Date : " + str(self.now.strftime("%Y-%m-%d %H:%M:%S")) + "\t\t\t\tInvoice No. : " + str(
            self.invoiceno) + "\t\t\tChecked Out By Administrator\n")
        print("SNo.\tItem\t\t\t\t\t\tQuantity\t\t\tPrice\n")


def main():
    mfv = Mfv()
    mfv.updatedates()
    # crt = Cart()

    countertoexit = 0
    while True:
        print("\t\t\tMonash Fruit and Vegetable Store\n")
        print("Date : " + str(mfv.now.date()) + "\t\t\t\tOrder No. : " + str(mfv.invoiceno) + "\t\t\t\tLogged in as Administrator\n")
        print("1. Checkout & Print Receipt")
        print("2. Daily Report")
        print("3. Display Local Supplier Stock")
        print("4. Display Overseas Supplier Stock")
        print("5. Exit Program")
        choice = int(input("Choose Option : "))
        if choice == 1:
            while True:
                print("1. Fruits")
                print("2. Vegetables")
                fruitorveg = int(input("Which would you like to add from : "))
                mfv.listitems(fruitorveg)
                itemnumber = int(input("Select item to add to cart : "))
                print("1. PrePacked")
                print("2. Weighted")
                packingtype = int(input("Choose Packing type : "))
                if packingtype == 1:
                    print("1. 5 KG Bag")
                    print("2. 10 KG Bag")
                    quantity = int(input("Which bag? : "))
                    mfv.additemtocart(itemnumber, fruitorveg, packingtype, quantity)
                elif packingtype == 2:
                    weight = int(input("Please specify weight (in KG) : "))
                    mfv.additemtocart(itemnumber, fruitorveg, packingtype, weight)
                print("1. Add More Items")
                print("2. Print Receipt")
                proceed = int(input("Choose to Proceed : "))
                if proceed == 1:
                    pass
                elif proceed == 2:
                    mfv.printreceipt()
                    mfv.invoiceno += 1
                    break
                else:
                    break

        elif choice == 2:
            print("\t\t\tMonash Fruit and Vegetable Store\n")
            print("\tDaily Report\n")

        elif choice == 3:
            print("\t\t\tMonash Fruit and Vegetable Store\n")
            print("\tLocal Supplier Stock\n")

        elif choice == 4:
            print("\t\t\tMonash Fruit and Vegetable Store\n")
            print("\tOverseas Supplier Stock\n")

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


if __name__ == "__main__":
    main()
