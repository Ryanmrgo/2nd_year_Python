elements=[10,20,0,40,15]
x=bytes(elements)
print(x)
print(x[0])
#elementsData=[2,-2,-3.3]
#y=bytes(elementsData)
#print(y)
a = "abc"
b = a.replace("a", "f")
print(b)
a = b"abc"
b = a.replace(b"a", b"f")
print(b)
print(b'Py' in b'Python')
print(b'1,2,3'.split(b','))
#[b'1', b'2', b'3']
print(b'1,2,3'.split(b',', maxsplit=1))
#[b'1', b'2,3']
print( b'1,2,,3,'.split(b','))
#[b'1', b'2', b'', b'3', b'']
print(b'ABCabc'.isalpha())
#True
print(b'ABCabc1'.isalpha())
#False
print(b'1234'.isdigit())
#True
print(b'1.3'.isdigit())
#False
v = memoryview(b'abcefg')
print(v[0])
#97
print(v[-1])
print(id(v))
#103
print(v[4])
#<memory at 0x7f3ddc9f4350>
print(bytes(v[1:4]))
#b'bce'



