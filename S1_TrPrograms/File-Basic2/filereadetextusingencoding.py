#File read, using Encoding
print("Testing for Encoding")
f1=open("guidobio.txt",mode='r',encoding='cp1252')
#f1=open("guidobio.txt",mode='r',encoding='utf-8')
#f1=open("myanmartest.txt",mode='r',encoding='utf-8')
#f1=open("myanmartest.txt",mode='r',encoding='cp1252')
#f1=open("myanmartest.txt",'r')
print(f1.read(),end='')
f1.close()
