from administrator import Administrator
from product import Product
import datetime


class Productlist:
    def __init__(self):
        self.admin = Administrator()
        self.product = Product()
        self.bag_type = 0
        self.discounted_price = 0
        self.now = datetime.datetime.now()
        self.cart = []
        self.itemname = []
        self.itemquantity = []
        self.itemprice = []
        self.invoiceno = 0
        self.totalprice = 0

    def __str__(self):
        self.invoiceno += 1
        print("\n\nDate : " + str(self.now.date()) + "\t\t\t\tOrder No. : " + str(self.invoiceno) + "\t\t\t\tLogged in as " + str(self.admin.admin_name) + "\n")
        print("Item Name" + "\t\t\t\t\t\t\t" + "Quantity" + "\t\t\t" + "Price")
        print("---------------------------------------------------------------------------------------")
        self.individualItems(self.cart)
        for x, y, z in zip(self.itemname, self.itemquantity, self.itemprice):
            print(" " + str(x) + "\t\t\t\t\t\t\t" + "|" + "\t\t" + str(y) + "\t\t\t" + "|" + "\t\t" + str(z) + "")
        print("---------------------------------------------------------------------------------------")
        self.totalprice = sum(self.itemprice)
        print("\t\t\t\t\t\t\t\t\t\t\t" + "Total Price = " + "\t" + str(self.totalprice) + "\n\n")

    def individualItems(self, listitem):
        length = 3
        i = [listitem[i::length] for i in range(length)]
        self.itemname = i[0]
        self.itemquantity = i[1]
        self.itemprice = i[2]
        return self.itemname, self.itemquantity, self.itemprice


# def main():
#     cart = Productlist()
#     print()
#
#
# if __name__ == "__main__":
#     main()
