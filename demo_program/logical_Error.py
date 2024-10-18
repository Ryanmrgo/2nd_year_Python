def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers) + 1  # incorrect calculation of average
    return average

def get_numbers_from_user():
    numbers = []
    num_count = int(input("Enter the number of elements: "))
    for i in range(num_count):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    return numbers

numbers = get_numbers_from_user()
average = calculate_average(numbers)
print(f"The average of the numbers is: {average}")