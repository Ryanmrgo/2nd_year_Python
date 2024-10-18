#Lecture 9

#Changing and Adding Elements to a List
datalist=[23,26,36,53,62]
print('data list tetst'+str(datalist[:]))
print('data list tetst',datalist[:])
print(type(datalist))

#Changing  Elements to a List
datalist[2]=60
datalist[4]=12
print('data list tetst2'+str(datalist[:]))


#Illustration of Adding Element to a list and list function
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


#show the index
print(datalist.index(53))


#list.pop
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.pop()
print ("list now : ", list1)

print ("list now : ", list1)
list1.pop(1)
print ("list now : ", list1)


#copy
list11 = ['physics', 'Biology', 'chemistry', 'maths','English']
list2=list11.copy()
print("copy of list11 is",list2)


