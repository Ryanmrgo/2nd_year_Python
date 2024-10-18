'''
#Testing Multiple inheritance

class Father:
    def gardening(self):
        print('I enjoy gardening')
class Mother:
    def cooking(self):
        print('I enjoy cooking')
class Child(Father,Mother):
    def sports(self):
        print('I enjoy sports')
c=Child()
c.sports()
c.gardening()
c.cooking()
'''

class Father:
    def skills(self):
        print('gardening and programming')
class Mother:
    def skills(self):
        print('cooking and arts')
class Child(Father,Mother):
    def skills(self):
        #Father.skills(self)
        #Mother.skills(self)
        #super().skills()
       # super().skills()
        print('sports')
c=Child()
c.skills()

###
