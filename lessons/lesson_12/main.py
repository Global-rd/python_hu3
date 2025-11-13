from cart_processor import process_cart_items

def main():

    shopping_cart = {
        "Timmy": [15, 32, 16, 17, 18],
        "Bob": [15, 32, 16],
        "Alice": [15, 2, 6, 7, 8],
    }

    for customer, prices in shopping_cart.items():
        process_cart_items(customer, prices)


if __name__ == "__main__":
    main()