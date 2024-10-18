'''
str="SampurneshBabu movie is excellent"

f=open("test_data.txt", "w")
f.write(str)
with open("test_data.txt", "r+") as f:
   text=f.read()
   print(text)
   print("The Current Cursor Position: ",f.tell())
   f.seek(24)
   print("The Current Cursor Position: ",f.tell())
   f.write("Britania Bisket")
   #print("The Current Cursor Position: ",f.tell())
   f.seek(0)
   text=f.read()
   #print("Data After Modification:")
   print(text)

 ''' 
'''
Syntax: f.seek(offset, fromwhere)
offset represents the number of positions.
The allowed values for second arguments are:
0 —> From beginning of file (default value)
1 —> From current position
2 —> From end of the file

io.UnsupportedOperation: can't do nonzero end-relative seeks
for fromwhere case 2,3
import os
use 'os.path.getsize' to obtain the file size
and then calculates the position to seek to.

you can open it in 'b’inary mode and seek() around.
'''

str="SampurneshBabu movie is excellent"
f=open("simple_data.txt", "w")
f.write(str)
with open("simple_data.txt", "rb") as f:
   '''
   #Read the entire file into memory
   content = f.read()
   file_size=len(content)
   print(file_size)
   print(f.tell())

   #file_size = os.path.getsize("simple_data.txt")
   '''
   content = f.read()
   print(content)
   f.seek(0)
   # Case 1: From the beginning of the file (fromwhere=0)
   f.seek(10, 0)    # Move 10 characters from the beginning
   data=f.read()
   print("After seeking 10, 0:",data)
   #f.seek(0)
   #print(f.tell())

   # Case 2: From the current position (fromwhere=1)
   f.seek(5, 1)  # Move 5 characters forward from the current position
   data=f.read()
   print("After seeking 5, 1:",data)
   
   #f.seek(0)
   
   # Case 3: From the end of the file (fromwhere=2)
   f.seek(-9, 2)  #Move 9 characters backward from the end
   data=f.read()
   print("After seeking -9, 2:",data)



