# CSE 2040 - Lecture 24 - 

# Example illustrating exception handling in Python

def read_from_file(filename):
        try:
                file_handle = open(filename,"r")
        except IOError:
                print("Error! File " + filename + " is not found!")
        else:
                line = file_handle.read()
                for word in line.split():
                     print(word)
                file_handle.close()
        
# Main
print()
filename = input("Enter the name of the file: ")
read_from_file(filename)
print()
