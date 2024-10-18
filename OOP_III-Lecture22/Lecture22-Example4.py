#illustration of adding ,modifying, deleting class attributes using built-in function
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
print(hasattr(I1,'code' )) #determine whether 'code' attribute exit or not
print(getattr(I1,'item')) # obtains the value of item attribute
setattr(I1,'price',35) #sets the new value to price
setattr(I1,'code',111) # set the new vaule to code
#I1.display()
delattr(I1,'code') #delete code attribute
print( 'after deleting'     ,I1.display())



      


