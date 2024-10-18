class Square:



class Rectangle(Square):
    


a, b=[float(x) for x in input("Enter two measurements: ").split()]
r=Rectangle(a,b)
r.area()
