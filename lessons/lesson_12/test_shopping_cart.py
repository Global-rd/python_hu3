import pytest
from shopping_cart import ShoppingCart
from unittest.mock import patch

@pytest.fixture
def empty_cart():
    return ShoppingCart()


def test_add_item(empty_cart):
    
    empty_cart.add_item("apple", 1, 2)
    
    assert empty_cart.items["apple"]["quantity"] == 2
    assert empty_cart.items["apple"]["price"] == 1

@pytest.mark.parametrize("item_name, price, quantity, expected_exception",
                         [
                             ("orange", -1, 1, ValueError), #negative price
                             ("orange", 1, 0, ValueError), #zero quantity
                             ("orange", 1, -2, ValueError), #zero quantity

                         ])
def test_add_item_invalid_input(empty_cart, item_name, price, quantity, expected_exception):

    with pytest.raises(expected_exception):
        empty_cart.add_item(item_name, price, quantity)

@patch("shopping_cart.ShoppingCart.get_discount_multiplier", return_value=0.1)
def test_checkout(mock_apply_discount, empty_cart):
    final_price = empty_cart.checkout("SAVE10")
    assert final_price == 0


#patch:  egy már létező függvény vagy objektum ideiglenes lecserélése egy kitalált verzióra
#mock: egy teljesen új objektum létrehozása csak a teszt miatt