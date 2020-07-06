from receipt import Receipt


class Report:
    def __init__(self):
        self.receipt = Receipt()
        self.report_id = 0
        self.total_revenue = 0
        self.total_revenue += self.receipt.total_price

    def __str__(self):
        pass

# def main():
#     pass
#
#
# if __name__ == "__main__":
#     main()
