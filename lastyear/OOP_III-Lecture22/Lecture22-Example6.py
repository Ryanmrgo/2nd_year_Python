#illustration of destroying objects using destructor method __del__()
class Inventory:
    'An inventory class'
    itemCount=0
    total_bill=0
    def __init__(self, item,price, quantity,code): #constructor
        self.item=item
        self.price=price
        self.quantity=quantity
        self.code=code
        Inventory.itemCount+=1
        print('No of object created',Inventory.itemCount)
    def __del__(self):
        Inventory.itemCount-=1
        print('No of object destroyed',Inventory.itemCount)

    def display(self):    #display info
        print('\n Item Name',self.item,'\nprice',self.price,'\n Quantity', self.quantity,'\n Total',self.total)



I1=Inventory('Soap','SP111',30.5,4)
I2=Inventory('Shampoo','SO001',130.5,2)
I3=Inventory('Olive Oil','OO002',80.5,1)
print('deleting I1')
del I1
print('deleting I2')
del I2
print('deleting I3',)
del I3





      


