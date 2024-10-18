datalist=[23,26,36,53,62]
#datalist=list([23,26,36,53,62])
#print('data list tetst'+str(datalist[:]))
#print('data list tetst',datalist[:])
print(type(datalist))
datalist[2]=60
#datalist[4]=12
#for i in range (len(datalist)):
 #   print(str(datalist[i]))
print('data list tetst2'+str(datalist[:]))
datalist=[23,45,31,53,62]
datalist.append(39)
print('test for append',datalist)
datalist.extend([76,23,15])
print('test for extend',datalist)
datalist.append(39)
print('data list tetst2')
print(datalist)
datalist.insert(2,62)
print('data list tetst3')
print(datalist)
datalist.remove(23)
print('data list tetst4')
print('test for remove',datalist)

