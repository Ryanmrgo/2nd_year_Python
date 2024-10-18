#illustration of built-in class attributes
class Inventory:
    'An inventory class'
    itemCount=0
    total_bill=0
    def __init__(self, item,price, quantity): #constructor
        self.item=item
        self.price=price
        self.quantity=quantity
        self.total=self.price*self.quantity
        Inventory.total_bill+=self.total
        Inventory.itemCount+=1

    def display(self):    #display info
        print('\n Item Name',self.item,'\nprice',self.price,'\n Quantity', self.quantity,'\n Total',self.total)



I1=Inventory('Soap',30.5,4)
print('\n test for dictionary')
print(Inventory.__dict__)
print('\n test for doc')
print(Inventory.__doc__)
print('\n test for name')
print(Inventory.__name__)
print('\n test for module')
print(Inventory.__module__)
print('\n test for bases')
print(Inventory.__bases__)
print('\n')




      


