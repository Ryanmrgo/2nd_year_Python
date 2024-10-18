while True:
    try:
        num = int(input("Enter three positive integer: "))
        print(num)
        if num < 100 or num >999:
            raise ValueError
        break
    except ValueError:
        print("Error.")

d1 = int(num / 100)
d2 = int(num/10)%10
d3 = num % 10

Even_count = 0
Odd_count = 0

if(d1 % 2 == 0):
    Even_count = Even_count+1
else:
    Odd_count = Odd_count+1

if(d2 % 2 == 0):
    Even_count = Even_count+1
else:
    Odd_count = Odd_count+1

if(d3 % 2 == 0):
    Even_count = Even_count+1
else:
    Odd_count = Odd_count+1

print("The input number has",Odd_count,"odd digits and",Even_count,"even digits.")

