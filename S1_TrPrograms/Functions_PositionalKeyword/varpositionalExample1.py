def generate_receipt(customer_name, *args):
    """
    Generate a receipt for a customer with variable items and prices.
    """
    print(f"Receipt for {customer_name}:")
    
    total_cost = 0
    for i in range(len(args)):
        item, price = args[i]
        print(f"{i + 1}. {item}: K{price:.2f}")
        total_cost += price

    print(f"\nTotal Cost: K{total_cost}")

# Example usage:
#generate_receipt("Mi Mi", ("Shirt", 19.99), ("Jeans", 29.99), ("Shoes", 49.99))
generate_receipt("Ma Ma", ("Book", 12.99), ("Notebook", 5.99), ("Pen Set", 8.49), ("Backpack", 39.99))
