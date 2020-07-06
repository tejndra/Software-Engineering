from product import Product
from productlist import Productlist
from report import Report

import datetime
from datetime import date
from datetime import timedelta
import random
import os


class POSController:
    def __init__(self):
        self.product = Product()
        self.productlist = Productlist()
        self.report = Report()

    def __str__(self):
        pass

    def tostring(self, listtoconvert):
        return ''.join(map(str, listtoconvert))

    def getLocalProductInfo(self):
        pass

    def getOverseasProductInfo(self):
        pass

    def checkInventory(self, itemno, itemtype, packtype, measure, supplier):
        if itemtype == 1:
            if packtype == 1 and measure == 1:
                if supplier == 1:
                    self.product.databank["Fruit"][itemno]["localinventory"] -= 5
                    return [self.tostring(list(self.product.databank["Fruit"][itemno].get("name"))), 5, self.product.databank["Fruit"][itemno].get("price")]
                else:
                    self.product.databank["Fruit"][itemno]["internationalinventory"] -= 5
                    return [self.tostring(list(self.product.databank["Fruit"][itemno].get("name"))), 5, self.product.databank["Fruit"][itemno].get("price")]

            elif packtype == 1 and measure == 2:
                if supplier == 1:
                    self.product.databank["Fruit"][itemno]["localinventory"] -= 10
                    return [self.tostring(list(self.product.databank["Fruit"][itemno].get("name"))), 10, self.product.databank["Fruit"][itemno].get("price")]
                else:
                    self.product.databank["Fruit"][itemno]["internationalinventory"] -= 10
                    return [self.tostring(list(self.product.databank["Fruit"][itemno].get("name"))), 10, self.product.databank["Fruit"][itemno].get("price")]

            elif packtype == 2:
                if supplier == 1:
                    self.product.databank["Fruit"][itemno]["localinventory"] -= measure
                    return [self.tostring(list(self.product.databank["Fruit"][itemno].get("name"))), measure, self.product.databank["Fruit"][itemno].get("price")]
                else:
                    self.product.databank["Fruit"][itemno]["internationalinventory"] -= measure
                    return [self.tostring(list(self.product.databank["Fruit"][itemno].get("name"))), measure, self.product.databank["Fruit"][itemno].get("price")]

        elif itemtype == 2:
            if packtype == 1 and measure == 1:
                if supplier == 1:
                    self.product.databank["Vegetable"][itemno]["localinventory"] -= 5
                    return [self.tostring(list(self.product.databank["Vegetable"][itemno].get("name"))), 5, self.product.databank["Fruit"][itemno].get("price")]
                else:
                    self.product.databank["Vegetable"][itemno]["internationalinventory"] -= 5
                    return [self.tostring(list(self.product.databank["Vegetable"][itemno].get("name"))), 5, self.product.databank["Fruit"][itemno].get("price")]

            elif packtype == 1 and measure == 2:
                if supplier == 1:
                    self.product.databank["Vegetable"][itemno]["localinventory"] -= 10
                    return [self.tostring(list(self.product.databank["Vegetable"][itemno].get("name"))), 10, self.product.databank["Vegetable"][itemno].get("price")]
                else:
                    self.product.databank["Vegetable"][itemno]["internationalinventory"] -= 10
                    return [self.tostring(list(self.product.databank["Vegetable"][itemno].get("name"))), 10, self.product.databank["Vegetable"][itemno].get("price")]

            elif packtype == 2:
                if supplier == 1:
                    self.product.databank["Vegetable"][itemno]["localinventory"] -= measure
                    return [self.tostring(list(self.product.databank["Vegetable"][itemno].get("name"))), measure, self.product.databank["Vegetable"][itemno].get("price")]
                else:
                    self.product.databank["Vegetable"][itemno]["internationalinventory"] -= measure
                    return [self.tostring(list(self.product.databank["Vegetable"][itemno].get("name"))), measure, self.product.databank["Vegetable"][itemno].get("price")]

    def addProduct(self, itemno, itemtype, packtype, measure, supplier):
        # self.productlist.cart = []
        self.productlist.cart += self.checkInventory(itemno, itemtype, packtype, measure, supplier)

    def getWeight(self):
        pass

    def calculateDiscount(self, expiringdate):
        pass

    def calculateTotalPrice(self):
        pass

    def generateReceipt(self, itemname, qty, price, packingtype):
        pass

    def calculateTotalRevenue(self):
        pass

    def generateReport(self):
        pass

    def updateDates(self):
        inventorycount = [100, 80, 90, 70, 110]
        listofsuppliers = self.product.suppliers
        item = 1
        for values in self.product.databank["Fruit"]:
            # self.product.databank["Fruit"][item]["stockdate"] = self.stockingdate
            # self.product.databank["Fruit"][item]["expirydate"] = self.stockingdate + timedelta(days=self.product.databank["Fruit"][item].get("shelflife"))
            self.product.databank["Fruit"][item]["localinventory"] = random.choice(inventorycount)
            self.product.databank["Fruit"][item]["internationalinventory"] = random.choice(inventorycount)
            self.product.databank["Fruit"][item]["supplier"] = random.choice(listofsuppliers)
            item += 1

        item = 1
        for values in self.product.databank["Vegetable"]:
            # self.product.databank["Vegetable"][item]["stockdate"] = self.stockingdate
            # self.product.databank["Vegetable"][item]["expirydate"] = self.stockingdate + timedelta(days=self.product.databank["Vegetable"][item].get("shelflife"))
            self.product.databank["Vegetable"][item]["localinventory"] = random.choice(inventorycount)
            self.product.databank["Vegetable"][item]["internationalinventory"] = random.choice(inventorycount)
            self.product.databank["Vegetable"][item]["supplier"] = random.choice(listofsuppliers)
            item += 1


# def main():
#     control = POSController()
#     control.updateDates()
#     control.addProduct(4, 1, 1, 1, 2)
#     print(control.productlist.cart)
#     control.addProduct(3, 2, 2, 4, 1)
#     print(control.productlist.cart)
#     control.addProduct(2, 1, 1, 1, 2)
#     print(control.productlist.cart)
#     control.addProduct(7, 2, 2, 4, 1)
#     print(control.productlist.cart)
#
#
# if __name__ == "__main__":
#     main()
