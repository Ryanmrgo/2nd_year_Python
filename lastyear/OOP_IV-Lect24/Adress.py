#e following example program:First create a Python program file by writing the following program in it:

 # create an address class in the program
class AddressClass:
     # define the components of the address class with default function
     def __init__(self, Street1, LiveinCity, LiveinState, PostalCode, Country, Street2 = ''):
         # defining components of address class as variables
         self.Street1 = Street1
         self.Street2 = Street2
         self.LiveinCity = LiveinCity
         self.LiveinState = LiveinState
         self.PostalCode = PostalCode
         self.Country = Country
     # define the properties of the address class with default function
     def __str__(self):
         TotalLines = [self.Street1]
         # using the if method to append the lines
         if self.Street2:
             lines.append(self.Street2)
         # printing following components in next line
         TotalLines.append(f'{self.LiveinCity}, {self.LiveinState} {self.PostalCode} {self.Country}')
         return '\n'.join(TotalLines) # appending the lines for output
# #import the python program script for the address class
# #from changing import AddressClass
 ## define the elements for the address class
Address1 = AddressClass('55 Main St.', 'Concord City', 'NH25', '03301', 'Mexico')
Address2 = AddressClass('36 Side St.', 'New Mexico City', 'NH67', '033207', 'Mexico')
 # print the address elements in the output
print('The first address element we added is: ')
print(Address1)
print('The second address element we added is: ')
print(Address2) 
