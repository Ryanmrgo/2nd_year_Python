# CSE 2040 - Lecture 20 - Example 3
# Example illustrating types of parameters

# var-positional parameters
def create_fruit_basket(*fruits):
     fruit_basket = list()
     for i in fruits:
          fruit_basket.append(i)
     return fruit_basket

print()
print("var-positional parameters:")
print("\tBasket contains: ",end=" ")
fruit_basket = create_fruit_basket("apple","mango","guava","pear","oranges")

numb_fruits = len(fruit_basket)
#print(numb_fruits)
#print(fruit_basket[numb_fruits-1])

for i in fruit_basket:
     print(i+",",end=" ")
     
print("---------------------------------------------------------------------")

