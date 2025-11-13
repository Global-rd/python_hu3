


class ShoppingCart:

    def __init__(self):
        self.items = {}

    
    def add_item(self, item_name, price, quantity):
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive!")

        if price < 0:
            raise ValueError("Price can not be negative!")
        
        if item_name in self.items:
            self.items[item_name]["quantity"] += quantity
        else:
            self.items[item_name] = {"price": price, "quantity": quantity}

    def remove_item(self, item_name, quantity):

        if item_name not in self.items:
            raise ValueError("Item not in cart")
        if quantity < 1:
            raise ValueError("Quantity must be positive!")

        if self.items[item_name]["quantity"] <= quantity:
            del self.items[item_name]
        else:
            self.items[item_name]["quantity"] -= quantity


    def get_total_cost(self):
        
        return sum(item["price"] * item["quantity"] for item in self.items.values())

    
    def get_discount_multiplier(self, discount_code):
        #in prod there would be an external service called for the valid codes (database)
        valid_codes = {"SAVE10": 0.1, "SAVE20": 0.2}
        discount = valid_codes.get(discount_code, 0)
        return discount


    def checkout(self, discount_code):

        if not self.items:
            return 0
        discounted_price = self.get_total_cost() * (1 - self.get_discount_multiplier(discount_code))
        return discounted_price
        

