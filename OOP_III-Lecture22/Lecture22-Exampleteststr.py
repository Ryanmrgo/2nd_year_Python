'''
#Test for str and repr
class Foo():
        def __init__(self):
            self.l = [{"Susan": ("Boyle", 50, "alive")}, {"Albert": ("Speer", 106, "dead")}]
        def __str__(self):
            ret_str = ""
            for d in self.l:
                for k in d:
                    ret_str += "".join([k, " ", d[k][0], " is ", str(d[k][1]), " and ", d[k][2], ". "])
            return ret_str
     
foo = Foo()
print (foo)

'''
# str and repr example program
s = 'Hello, Good Morning.'
print (str(s))
print(type(s))
print( str(2.0/11.0))
print( type(str(2.0/11.0)))

s = 'Hello, Good Morning.'
print( repr(s) )
print(type(s))
print( repr(2.0/11.0))
print (type(repr(2.0/11.0)) )


# Python program to demonstrate writing of __repr__ and 
# __str__ for user defined classes 
  
# A user defined class to represent Complex numbers 
class Complex: 
  
    # Constructor 
    def __init__(self, real, imag): 
       self.real = real 
       self.imag = imag 
  
    # For call to repr(). Prints object's information 
    def __repr__(self): 
       return 'Rational(%s, %s)' % (self.real, self.imag)     
  
    # For call to str(). Prints readable form 
    def __str__(self): 
       return '%s + i%s' % (self.real, self.imag)     
  
  
# Driver program to test above 
t = Complex(10, 20) 
  
print ('Result from str',str(t))  # Same as "print t" 
print ('Result from repr',repr(t)) 


