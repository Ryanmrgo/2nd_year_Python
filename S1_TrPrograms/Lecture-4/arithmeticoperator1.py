#example1
#Can you create a program to convert distance in kilometers to miles?

#Formula: 1 kilometer -> 0.621371 miles

# Program to convert kilometers to files

distance_km = 564.5

conversion_ratio = 0.621371

distance_miles = distance_km * conversion_ratio

print(distance_miles) # 350.7639295

#Suppose you are a university student, and you need to pay 4535 dollars
#tuition fee for the next semester.
#The college is giving you a discount of 10% on the early payment
#of your tuition fee. Since it's a good offer, you decided to make
#an early payment. Can you find out how much money you have to pay?

fee = 4530

discount_percent = 10
discount_amount = discount_percent/100*fee
discounted_fee = fee - discount_amount

print("Fee after discount:", discounted_fee, "dollars")  # 4081.5
