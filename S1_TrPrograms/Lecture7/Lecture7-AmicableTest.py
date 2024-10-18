x=int(input('Enter num1'))
y=int(input('Enter num1'))
sum_x=0
sum_y=0
for i in range(1,x):
    if((x%i)==0):
        sum_x=sum_x+i
for j in range(1,y):
    if((y%i)==0):
        sum_y=sum_y+i
if(sum_x==y and sum_y==x):
   print("They are amicable numbers",x,y)
else:
    print("No they are not amicable",x,y)
   
    
