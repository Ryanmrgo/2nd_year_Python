def total_two_fractions(num1, den1, num2, den2):
    """
    Calculate the sum of two fractions.

    Parameters:
    - num1 (int): Numerator of the first fraction
    - den1 (int): Denominator of the first fraction
    - num2 (int): Numerator of the second fraction
    - den2 (int): Denominator of the second fraction

    Returns:
    tuple: Tuple containing the numerator and denominator of the sum
    """
    result_num = num1 * den2 + num2 * den1
    result_den = den1 * den2
    return result_num, result_den

result1 = total_two_fractions(1, 2, 3, 4)
result2 = total_two_fractions(num1=5, den1=6, num2=7, den2=8)
result3 = total_two_fractions(1, den1=3, num2=4, den2=5)

print(f"Result 1: {result1[0]}/{result1[1]}")
print(f"Result 2: {result2[0]}/{result2[1]}")
print(f"Result 3: {result3[0]}/{result3[1]}")