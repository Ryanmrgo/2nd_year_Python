# CSE 2040 - Lecture 19 - Example 1
# Example illustrating  definition of a function in Python

# Function to find if a word is palindrome or not
def isPalindrome_CStyle(word):
     ''' Function that finds if the input parameter is a palindrome or not '''
     print('Using C Style function!')
     length = len(word)
     i = 0
     j = -1
     while i <length / 2:
          if word[i] == word[j]:
               i = i + 1
               j = j - 1
          else:
               break
     if i  >= length / 2:
          return True
     else:
          return False

def isPalindrome_PythonStyle(word):
     ''' Function that finds if the input parameter is a palindrome or not '''
     print('Using Python Style function!')
     if (word == word[::-1]): # Give the reverse of the string
          return True
     else:
          return False
  
print("-------------------------------------------------------")
word = input('Input a word:')
if isPalindrome_CStyle(word) == True:
     print('Input word is a palindrome')
else:
     print('Input word is not a palindrome')

print("-------------------------------------------------------")

if isPalindrome_PythonStyle(word) == True:
     print('Input word is a palindrome')
else:
     print('Input word is not a palindrome')

print("-------------------------------------------------------")

print()

