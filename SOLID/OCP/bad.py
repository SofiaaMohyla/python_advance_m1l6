class DiscountCalculator():
    def __init__(self, product_type, cost):
        self.product_type = product_type
        self.cost = cost

    def get_discounted_price(self):
        if self.product_type == "SHIRT":
            return self.cost - (self.cost * 0.10)
        elif self.product_type == "TSHIRT":
            return self.cost - (self.cost * 0.15)
        elif self.product_type == "PANT":
            return self.cost - (self.cost * 0.25)


dc_Shirt = DiscountCalculator("SHIRT", 100)
print(dc_Shirt.get_discounted_price())

dc_TShirt = DiscountCalculator("TSHIRT", 100)
print(dc_TShirt.get_discounted_price())

dc_Pant = DiscountCalculator("PANT", 100)
print(dc_Pant.get_discounted_price())
