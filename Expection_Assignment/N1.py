def SOTF(n1, d1, n2, d2):
    try:
        
        if d1 != 0 and d2 != 0:
            CD = d1 * d2
            Sum = (n1 * d2 + n2 * d1)

            return Sum, CD
        else:
            print("Error: Division by zero error.")
            return None, None
    except ZeroDivisionError:
        print("Error: Zero division by zero error.")
        return None, None

n1, d1, n2, d2 = 1, 2, 1, 3
result1, CD1 = SOTF(n1, d1, n2, d2)
if result1 is not None and CD1 is not None:
    print(f"Sum of {n1}/{d1} and {n2}/{d2} is: {result1}/{CD1}")

n1, d1, n2, d2 = 3, 4, 2, 5
result2, CD2 = SOTF(n1, d1, n2, d2)
if result2 is not None and CD2 is not None:
    print(f"Sum of {n1}/{d1} and {n2}/{d2} is: {result2}/{CD2}")

n1, d1, n2, d2 = 1, 0, 2, 3
result3, CD3 = SOTF(n1, d1, n2, d2)
if result3 is not None and CD3 is not None:
    print(f"Sum of {n1}/{d1} and {n2}/{d2} is: {result3}/{CD3}")
