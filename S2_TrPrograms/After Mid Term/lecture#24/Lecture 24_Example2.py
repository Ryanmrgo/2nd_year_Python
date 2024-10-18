#Lecture 24 - Example 2

# Higher order function - Another example - ACCEPTING A FUNCTION AS A PARAMETER

def printList(fetchList):
    list = fetchList()
    for item in range(len(list)):
        print(list[item])
        
def getStudentList():
    ''' Gets list of students from ... '''
    studentList = ["Peter", "Chang", "John", "Cilic"]
    return studentList

def getCourseList():
    ''' Gets list of courses from ... '''
    courseList = ["Programming III", "Discrete Mathematics", "Computer Organization"]
    return courseList

def getRoomList():
    ''' Gets list of rooms from ... '''
    roomList = ["Room 201", "Room 202", "Room 203", "Room 204", "Room 208", "Room 209", "Room 210"]
    return roomList

# Main
print()
print("Which list should be printed:")
print("\t1. Student List")
print("\t2. Course List")
print("\t3. Room List")
print()
while (True):
    choice = int(input("Enter your choice - 1, 2 or 3: "))
    if (choice < 1 or choice > 3):
        print("Input not valid! Enter only 1, 2 or 3")
        print()
        continue
    else:
        break
print()
print("Your choice is " + str(choice))

print()
if (choice == 1):   
    print("List of students ...")
    printList(getStudentList)
elif (choice == 2):
    print("List of courses ...")
    printList(getCourseList)
else:
    print("List of rooms ...")
    printList(getRoomList)
print()
