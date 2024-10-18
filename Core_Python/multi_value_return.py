def Operations (a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    mod=a%b
    div=round(a/b,2)
    #round is the pyhon function that can cut float value into desire floating point .
    #Fore value indicate the float oraginal value and the the back is the number of float position that you wat to get 

    return sum,sub,mul,mod,div

tuple=Operations(2,3)

print("The result are:")
for i in tuple:
 print(i,end=',')


    