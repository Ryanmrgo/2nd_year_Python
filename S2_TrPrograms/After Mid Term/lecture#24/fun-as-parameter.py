def getStudentList():
    studentList = ["x1","x2","x3","x4"]
    return studentList
def getCourseList():
    courseList = ["CSE-2040", "CSE-5036", "CSE-1020"]
    return courseList
def printList(fetchList):
    list=fetchList()
    for item in range(len(list)):
        print(list[item])

#function as parameter
printList(getStudentList)
printList(getCourseList)
