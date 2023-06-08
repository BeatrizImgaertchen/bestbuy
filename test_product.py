import pytest
from products import Product


def test_create_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2", "Incorrect product name"
    assert product.price == 1450, "Incorrect product price"
    assert product.quantity == 100, "Incorrect product quantity"
    assert product.is_active(), "Product should be active"


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError, match="Invalid name"):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product("MacBook Air M2", price=-1450, quantity=100)


def test_product_quantity_zero():
    product = Product("MacBook Air M2", price=1450, quantity=0)
    assert not product.is_active(), "Product should be inactive"


def test_product_purchase():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(50)
    assert total_price == 72500, "Incorrect total price"
    assert product.quantity == 50, "Incorrect updated quantity"


def test_product_purchase_with_insufficient_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(Exception, match="Invalid quantity"):
        product.buy(150)
