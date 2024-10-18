
# (name, $-income)
customers = [("John", 240000),
             ("Alice", 120000),
             ("Ann", 1100000),
             ("Zach", 44000)]
# your high-value customers earning <$1M
whales = []
for customer, income in customers:
    if income>1000000:
        whales.append(customer)
print(whales)

whales = [x for x,y in customers if y>1000000]
print(whales)
