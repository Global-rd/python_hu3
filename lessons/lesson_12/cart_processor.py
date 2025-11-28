
def calculate_total(prices):

    return sum(prices)


def process_cart_items(customer_name, prices):
    total_price = calculate_total(prices)
    print(f"Total prices for {customer_name}: ${total_price:.2f}")
    return total_price