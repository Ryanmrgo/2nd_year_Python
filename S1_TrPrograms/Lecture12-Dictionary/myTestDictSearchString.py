dict={}
str='Core Python is a kind Python Programming Book'
for x in str:
    dict[x]=dict.get(x,0)+1
for k,v in dict.items():
    print('Key={}\t its occurence of={}'.format(k,v))
