
#Multiple Inheritance using super

class Parent(object):
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number


class ChildA(Parent):
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number
        super(ChildA, self).__init__(name = self.name, serial_number = self.serial_number)

    def speak(self):
        print("I am from Child A")


class ChildB(Parent):
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number
        super(ChildB, self).__init__(name = self.name, serial_number = self.serial_number)

    def speak(self):
        print("I am from Child B")
    def display(self):
        return (str(self.name)+'\t' + str(self.serial_number))

class GrandChild(ChildA, ChildB):
    def __init__(self, a_name, b_name, a_serial_number, b_serial_number):
        self.a_name = a_name
        self.b_name = b_name
        self.a_serial_number = a_serial_number
        self.b_serial_number = b_serial_number
        super(GrandChild, self).__init__(a_name, b_name )
    def display(self):
        return (str(self.a_name)+'\t' + str(self.b_name)+'\t'+str(self.a_serial_number)+'\t' + str(self.b_serial_number))

P=Parent('U Mya','S001')
CA=ChildA('U Min','S002')
CB=ChildB('U Aung','S003')
G=GrandChild('Naung Naung','s004','s002','s003')
G.speak()
print(G.display())
print(CB.display())

G.display()

