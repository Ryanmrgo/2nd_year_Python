import threading
import time

# Define a coffee counter class
class CoffeeCounter:
    def __init__(self):
        self.counter = 0
        self.total_coffee_to_produce = 15
        self.coffee_available = False

    def produce_coffee(self):
        while self.counter <= self.total_coffee_to_produce:
            if not self.coffee_available:
                self.counter += 1
                coffee_cup = f"Coffee Cup #{self.counter}"
                print(f"Produced: {coffee_cup}")
                self.coffee_available = True
            time.sleep(1)  # Simulate coffee production time

    def serve_coffee(self):
        while self.counter <= self.total_coffee_to_produce:
            if self.coffee_available:
                coffee_cup = f"Coffee Cup #{self.counter}"
                print(f"Served: {coffee_cup}")
                self.coffee_available = False
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
