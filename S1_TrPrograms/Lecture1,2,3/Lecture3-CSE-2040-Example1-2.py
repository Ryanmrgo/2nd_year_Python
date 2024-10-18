#Lecture5- Test vale,variable name, Memory Location Test
#id test and type test
print('Testing1 for same varialble name,different data type,same value and'
      +'different memo location is')
x=10
print(id(x))
x=20
print(id(x))
x=20.8
print(id(x))
x='Hello World'
print(id(x))
x=10
print(id(x))
x=20
print(id(x))

print('Testing2 for different variable name and same value and'
      + 'same memory location is')


x=y=z=50
print(id(x))
print(id(y))
print(id(z))

print('Testing3 for  differnt variable name and'
      +'different data types and differnt memory location is')
x,y,z=10,2.34,'Hello World'
print(id(x))
print(id(y))
print(id(z))
print('Testing 4 for same value'
      +'same name but another place in a program but same memory location')
x=10
y=23.09
z=5j
print(type(x))
print(type(y))
print(type(z))

      

      
      
      
