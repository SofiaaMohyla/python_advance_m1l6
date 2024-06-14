from abc import ABC, abstractmethod


class DiscountCalculator(ABC):
    @abstractmethod
    def get_discounted_price(self):
        pass


class DiscountCalculatorShirt(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.10)


class DiscountCalculatorTshirt(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.15)


class DiscountCalculatorPant(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.25)


dc_Shirt = DiscountCalculatorShirt(100)
print(dc_Shirt.get_discounted_price())

dc_TShirt = DiscountCalculatorTshirt(100)
print(dc_TShirt.get_discounted_price())

dc_Pant = DiscountCalculatorPant(100)
print(dc_Pant.get_discounted_price())
