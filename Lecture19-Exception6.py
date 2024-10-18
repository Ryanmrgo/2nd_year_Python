# CSE 2040 - Lecture 23

# Example illustrating exception handling in Python

def read_from_file(filename):
        ''' Read from file to show exception handling '''
        try:
                assert "py" in filename
        except AssertionError:
                print("Only .py files are accepted")
        else:
                try:
                        file_handle = None
                        file_handle = open(filename,"r")
                        line = file_handle.read()
                        for word in line.split():
                             print(word)
                        try:
                                file_handle.write("Adding a new line")
                        except IOError:
                                print("Error! File " + filename + " is not writable")
                except IOError:
                        print()
                        print("Error! File " + filename + " is not found!")
                finally:
                        if (file_handle is not None):
                                file_handle.close()      
        
# Main
print()
filename = input("Enter the name of the file: ")
read_from_file(filename)
print()
