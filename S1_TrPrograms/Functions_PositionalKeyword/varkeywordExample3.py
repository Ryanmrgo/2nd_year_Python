def calculate_total_cost(**kwargs):
    """
    Calculate the total cost of items in a shopping cart.
    """
    total_cost = 0
    print("Shopping Cart:")
    for item, price in kwargs.items():
        print(f"{item}: ${price}")
        total_cost += price
    print(f"\nTotal Cost: ${total_cost}")

# Example usage:
calculate_total_cost(apple=1.5, banana=0.75, laptop=999.99)
calculate_total_cost(shirt=19.99, shoes=49.99, socks=5.99, hat=12.99)
calculate_total_cost(book=15.99, pen=2.49, notebook=4.99, headphones=39.99)
