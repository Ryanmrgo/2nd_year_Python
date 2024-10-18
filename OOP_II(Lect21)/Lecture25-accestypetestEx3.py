# Testing access types

class BaseClass:
     ''' Just for testing '''

     def __init__(self, d1, d2, d3):
          self.__privateData = d1
          self._protectedData = d2
          self.publicData = d3

     def __setPrivateData(self, d1):
          privateData = d1

     def _setProtectedData(self, d2):
          self.__setPrivateData(200)
          self.setPublicData(210)
          self._protectedData = d2

     def setPublicData(self, d3):
          protectedData = 10
          publicData = d3

bc = BaseClass(10,20,30)

print(bc)
print(bc._protectedData)
print(bc.publicData)
#print(bc.__privateData)#Error
print(bc._BaseClass__privateData)#Name Mangling is done here

bc._BaseClass__setPrivateData(100)

bc._setProtectedData(2020)

print(bc._protectedData)
print(bc.publicData)







