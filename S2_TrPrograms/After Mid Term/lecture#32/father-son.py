'''
class Father:
    def __init__(self):
        self.property=80000

    def display_property(self):
        print("Father\'s property: ",self.property)

class Son(Father):
    pass


s=Son()
s.display_property()

#constructor overriding and method overriding(exactly the same name as that of super class)
class Father:
    def __init__(self):
        self.property=80000

    def display_property(self):
        print("Father\'s property: ",self.property)

class Son(Father):
    def __init__(self):
        self.property=20000
        
    def display_property(self):
        print("Son\'s property: ",self.property)


s=Son()
s.display_property()
'''

class Father:
    def __init__(self,property1):
        self.property1=property1

    def display_property(self):
        print("Father\'s property: ",self.property1)

class Son(Father):
    def __init__(self,property1,property2):
        super().__init__(property1)
        self.property2=property2
        
        
    def display_property(self):
        print("Son\'s property: ",self.property2)
        super().display_property()
        print("Total property of child: ",self.property1+self.property2)


s=Son(80000,20000)
s.display_property()
