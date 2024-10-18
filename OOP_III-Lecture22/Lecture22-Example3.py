#illustration of adding ,modifying, deleting class attributes
class Inventory:
    #An inventory class
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
#I2=Inventory('Shampoo',130.5,2)
#I3=Inventory('Olive Oil',80.5,1)
#I1.display()
#I2.display()
#I3.display()

I1.code=111 #adding new attribute
I1.price=29.0 #modifying the price attribute
I1.display() #display update value of I1 object

del I1.code
print('after deletion',I1.display())
print(' \n Total no of items',Inventory.itemCount)
print(' \n Total bills',Inventory.total_bill)


