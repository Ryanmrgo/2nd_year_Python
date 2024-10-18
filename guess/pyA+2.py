 1.Prime Numbers:


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage:
num = 17
print(is_prime(num))  # Output: True

2.GCD (Greatest Common Divisor):



def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage:
num1 = 48
num2 = 18
print(gcd(num1, num2))  # Output: 6

3.LCM (Least Common Multiple):



def lcm(a, b):
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)
    return (a * b) // gcd(a, b)

# Example usage:
num1 = 12
num2 = 18
print(lcm(num1, num2))  # Output: 36

4.Reverse a String:



def reverse_string(s):
    return s[::-1]

# Example usage:
input_string = 'Hello, World!'
print(reverse_string(input_string))  # Output: '!dlroW ,olleH'

5.Factorial:



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
num = 5
print(factorial(num))  # Output: 120

6.Fibonacci Sequence:



def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

# Example usage:
num_terms = 8
print(fibonacci(num_terms))  # Output: [0, 1, 1, 2, 3, 5, 8, 13]

7.Palindrome:



def is_palindrome(s):
    clean_str = ''.join(char.lower() for char in s if char.isalnum())
    return clean_str == clean_str[::-1]

# Example usage:
input_str = 'A man, a plan, a canal, Panama!'
print(is_palindrome(input_str))  # Output: True

8.Count Vowels:



def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Example usage:
input_str = 'Hello, World!'
print(count_vowels(input_str))  # Output: 3

9.Unique Elements:



def get_unique_elements(arr):
    return list(set(arr))

# Example usage:
input_array = [1, 2, 3, 2, 4, 5, 1]
print(get_unique_elements(input_array))  # Output: [1, 2, 3, 4, 5]

10.Check for Anagrams:



def are_anagrams(str1, str2):
    clean_str1 = ''.join(char.lower() for char in str1 if char.isalnum())
    clean_str2 = ''.join(char.lower() for char in str2 if char.isalnum())
    return sorted(clean_str1) == sorted(clean_str2)

# Example usage:
word1 = 'listen'
word2 = 'silent'
print(are_anagrams(word1, word2))  # Output: True

11.Remove Duplicates:



def remove_duplicates(arr):
    return list(set(arr))

# Example usage:
array_with_duplicates = [1, 2, 3, 2, 4, 5, 1]
print(remove_duplicates(array_with_duplicates))  # Output: [1, 2, 3, 4, 5]

12.Title Case a Sentence:



def title_case(sentence):
    return sentence.title()

# Example usage:
input_sentence = 'this is a sample sentence'
print(title_case(input_sentence))  # Output: 'This Is A Sample Sentence'

13.Max and Min in Array:



def find_max_and_min(arr):
    max_num = max(arr)
    min_num = min(arr)
    return {'max': max_num, 'min': min_num}

# Example usage:
numbers_array = [3, 1, 7, 4, 10, 2]
print(find_max_and_min(numbers_array))  # Output: {'max': 10, 'min': 1}

14.Capitalize First Letter:



def capitalize_first_letter(s):
    return s.capitalize()

# Example usage:
input_str = 'hello, world!'
print(capitalize_first_letter(input_str))  # Output: 'Hello, world!'

15.Check for a Substring:



def contains_substring(full_string, substring):
    return substring in full_string

# Example usage:
main_string = 'JavaScript is awesome'
sub_string = 'is'
print(contains_substring(main_string, sub_string))  # Output: True

16.Binary to Decimal:



def binary_to_decimal(binary_string):
    return int(binary_string, 2)

# Example usage:
binary_number = '101010'
print(binary_to_decimal(binary_number))  # Output: 42

17.Reverse Words in a Sentence:



def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# Example usage:
input_sentence = 'This is a sample sentence'
print(reverse_words(input_sentence))  # Output: 'sentence sample a is This'

18.Chunk an Array:



def chunk_array(arr, chunk_size):
    return [arr[i:i+chunk_size] for i in range(0, len(arr), chunk_size)]

# Example usage:
input_array = [1, 2, 3, 4, 5, 6, 7, 8]
print(chunk_array(input_array, 3))  # Output: [[1, 2, 3], [4, 5, 6], [7, 8]]

19.Shuffle an Array:



import random

def shuffle_array(arr):
    random.shuffle(arr)
    return arr

# Example usage:
input_array = [1, 2, 3, 4, 5]
print(shuffle_array(input_array))  # Output: [3, 1, 5, 4, 2] (random order)

20.Validate Email Address:



import re

def is_valid_email(email):
    regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(regex, email) is not None

# Example usage:
email_address = 'user@example.com'
print(is_valid_email(email_address))  # Output: True

21.Find the Longest Word:



def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example usage:
input_sentence = 'This is a sample sentence'
print(find_longest_word(input_sentence))  # Output: 'sentence'

22. Capitalize Each Word:



def capitalize_each_word(sentence):
    return sentence.title()

# Example usage:
input_sentence = 'this is a sample sentence'
print(capitalize_each_word(input_sentence))  # Output: 'This Is A Sample Sentence'

23.Check for Armstrong Number:



def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_digits == num

# Example usage:
number = 153
print(is_armstrong_number(number))  # Output: True

24. Flatten Nested Arrays:



def flatten_array(nested_array):
    flattened_array = []
    for sublist in nested_array:
        if isinstance(sublist, list):
            flattened_array.extend(flatten_array(sublist))
        else:
            flattened_array.append(sublist)
    return flattened_array

# Example usage:
nested_array = [1, [2, [3, 4], 5], 6]
print(flatten_array(nested_array))  # Output: [1, 2, 3, 4, 5, 6]

25.Find Second Largest Element:



def find_second_largest(arr):
    unique_sorted = sorted(set(arr), reverse=True)
    return unique_sorted[1]

# Example usage:
numbers_array = [5, 3, 9, 7, 1, 8]
print(find_second_largest(numbers_array))  # Output: 8

26. Check for a Leap Year:



def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage:
year = 2024
print(is_leap_year(year))  # Output: True

27.Remove Whitespace:



def remove_whitespace(str):
    return ''.join(str.split())

# Example usage:
string_with_whitespace = '  Hello, World!  '
print(remove_whitespace(string_with_whitespace))  # Output: 'Hello,World!'

28.Count Consonants:



def count_consonants(str):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return sum(1 for char in str if char in consonants)

# Example usage:
input_str = 'Hello, World!'
print(count_consonants(input_str))  # Output: 8

29.Find Median of Array:



def find_median(arr):
    sorted_arr = sorted(arr)
    n = len(arr)
    if n % 2 == 0:
        return (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    else:
        return sorted_arr[n // 2]

# Example usage:
numbers_array = [3, 1, 7, 4, 10, 2]
print(find_median(numbers_array))  # Output: 3.5
