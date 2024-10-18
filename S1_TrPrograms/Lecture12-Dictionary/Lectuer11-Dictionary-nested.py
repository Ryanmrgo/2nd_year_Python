#iterating through nested
people = {1: {'Name': 'John', 'Age': '27', 'Gender': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Gender': 'Female'}}
'''     
for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    for key in p_info:
        print(key + ':', p_info[key])
       
'''
for x,y in people.items():
    print("\nPerson ID:", x)
    for key in y:
        print(key + ':', y[key])

   
