def printStudentProfile(**kwarg):
    for key, value in kwarg.items():
        print("{} is {}".format(key, value))
#printStudentProfile(**{'Name': 'Doraemon', 'Age': 8})
#printStudentProfile(**{'Name': 'Nobita', 'Age': 8, 'Gender': 'Male'})
printStudentProfile(**{'Name': 'Aye Aye', 'Age': 18, 'Gender': 'Female','Rollno':12,'Academadic Year':2023})
