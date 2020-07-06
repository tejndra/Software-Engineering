from supplier import Supplier


class Product:
    def __init__(self):
        self.databank = {
            "Fruit": {
                1:
                    {"name": "Apple",
                     "shelflife": 9,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                2:
                    {"name": "Banana",
                     "shelflife": 4,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                3:
                    {"name": "Blueberry",
                     "shelflife": 7,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                4:
                    {"name": "Cherry",
                     "shelflife": 4,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                5:
                    {"name": "Grapes",
                     "shelflife": 5,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                6:
                    {"name": "Orange",
                     "shelflife": 7,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                7:
                    {"name": "Pineapple",
                     "shelflife": 5,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                8:
                    {"name": "Pear",
                     "shelflife": 7,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                9:
                    {"name": "Strawberry",
                     "shelflife": 4,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                10:
                    {"name": "Watermelon",
                     "shelflife": 7,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     }
            },
            "Vegetable": {
                1:
                    {"name": "Beetroot",
                     "shelflife": 9,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                2:
                    {"name": "Cabbage",
                     "shelflife": 9,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                3:
                    {"name": "Carrot",
                     "shelflife": 9,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                4:
                    {"name": "Cauliflower",
                     "shelflife": 7,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                5:
                    {"name": "Corn",
                     "shelflife": 4,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                6:
                    {"name": "Cucumber",
                     "shelflife": 5,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                7:
                    {"name": "Onion",
                     "shelflife": 9,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                8:
                    {"name": "Potato",
                     "shelflife": 9,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                9:
                    {"name": "Spinach",
                     "shelflife": 7,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     },
                10:
                    {"name": "Tomato",
                     "shelflife": 7,
                     "price": 2,
                     "localinventory": None,
                     "internationalinventory": None,
                     "supplier": None,
                     "stockdate": None,
                     "expirydate": None
                     }
            }
        }
        self.supplier = Supplier()
        self.suppliers = self.supplier.supplier_name

    def __str__(self):
        pass


# def main():
#     prod = Product()
#     print(prod.databank)
#
#
# if __name__ == "__main__":
#     main()
