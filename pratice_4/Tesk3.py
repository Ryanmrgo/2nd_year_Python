def total_many_fractions(*fractions):
    """
    Calculate the sum of multiple fractions.

    Parameters:
    - fractions (int): Pairs of numerators and denominators representing fractions

    Returns:
    tuple: Tuple containing the numerator and denominator of the sum
    """
    result_num = 0
    result_den = 1

    for i in range(0, len(fractions), 2):
        num = fractions[i]
        den = fractions[i + 1]
        result_num = result_num * den + num * result_den
        result_den *= den

    return result_num, result_den

result = total_many_fractions(1, 2, 3, 4, 1, 3, 2, 5, 5, 6)

print(f"Sum of fractions: {result[0]}/{result[1]}")
