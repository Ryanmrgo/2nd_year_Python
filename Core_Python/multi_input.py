def calculate(lst):
    n=len(lst)
    sum=0
    for i in lst:
       sum=sum+i
       avg=sum/n
    return sum,avg

#lst = [x for x in input('Enter strings separated by comma:').split(',')]
#space ma pr chin yin "" ma htal nal int lo chin yin x ko a shy ka int htal
lst = [int(x) for x in input('Enter numbers seperated by comma:').split(',')]

x,y=calculate(lst)
print('Total:',x)
print("Average:",y)