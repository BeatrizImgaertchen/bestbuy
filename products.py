from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentageDiscountPromotion(Promotion):
    def __init__(self, name, discount_percentage):
        super().__init__(name)
        self.discount_percentage = discount_percentage

    def apply_promotion(self, product, quantity):
        price = product.price * quantity
        discount = price * (self.discount_percentage / 100)
        return price - discount


class SecondItemHalfPricePromotion(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity < 2:
            return product.price * quantity
        else:
            price = product.price * ((quantity // 2) + (quantity % 2))
            return price


class Buy2Get1FreePromotion(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity < 3:
            return product.price * quantity
        else:
            price = product.price * ((quantity // 3) * 2 + (quantity % 3))
            return price


class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Invalid name")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_promotion(self, promotion):
        self.promotion = promotion

    def show(self):
        promotion_info = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promotion_info}"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if not self.active:
            raise Exception("Product is not active")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return self.price * quantity


def main():
    laptop = Product("MacBook Pro", price=2000, quantity=10)
    headphones = Product("Bose Noise Cancelling Headphones", price=300, quantity=5)

    discount_promotion = PercentageDiscountPromotion("20% off", discount_percentage=20)
    laptop.set_promotion(discount_promotion)

    second_item_promotion = SecondItemHalfPricePromotion("Second item at half price")
    headphones.set_promotion(second_item_promotion)

    print(laptop.show())
    print(headphones.show())

    print(laptop.buy(2))
    print(headphones.buy(3))


if __name__ == "__main__":
    main()

