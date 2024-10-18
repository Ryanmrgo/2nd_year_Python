import threading
import time

# Define a coffee counter class
class CoffeeCounter:
    def __init__(self):
        self.counter = 0
        self.total_coffee_to_produce = 15

    def produce_coffee(self):
        while self.counter < self.total_coffee_to_produce:
            self.counter += 1
            coffee_cup = f"Coffee Cup #{self.counter}"
            print(f"Produced: {coffee_cup}")
            time.sleep(1)  # Simulate coffee production time

    def serve_coffee(self):
        while self.counter < self.total_coffee_to_produce:
            coffee_cup = f"Coffee Cup #{self.counter}"
            print(f"Served: {coffee_cup}")
            time.sleep(0.5)  # Simulate time taken to serve coffee

# Create a coffee counter instance
coffee_counter = CoffeeCounter()

# Create producer and consumer threads
producer_thread = threading.Thread(target=coffee_counter.produce_coffee)
consumer_thread = threading.Thread(target=coffee_counter.serve_coffee)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()

print("Coffee production and consumption complete.")
