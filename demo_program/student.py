from teacher import Teacher

class Student (Teacher):
    def set_mark(self,mark):
        self.mark=mark
    def get_mark(self):
        return self.mark
    

s=Student()
s.set_id("001")
s.set_name("Rakesh")
s.set_address("MIIT,Mandalay")
s.set_mark(40)


print("ID:",s.get_id())
print("Name:",s.get_name())
print("Address:",s.get_address())
print("Mark:",s.get_mark())

