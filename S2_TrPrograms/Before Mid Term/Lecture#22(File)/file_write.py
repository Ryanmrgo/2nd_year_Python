'''File Object Properties and File Write :
      write(str) - single line
      writelines(str)'''
'''
f=open("abc.txt", 'w')
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
print("Is File Closed : ", f.closed)
f.close()
print("Is File Closed : ", f.closed)

#file write operation
f=open("wish.txt", 'w')
f.write("Welcome\nto\npython world\n")
f.write("Welcome to python world\n")
print("Data written to the file successfully")
f.close()

#append operation
f=open("wish.txt", 'a')
f.write("Python is a great language.\nYeah its great!!\n")
print("Data written to the file successfully")
f.close()
'''
#File write (mutiple lines)
f=open("names.txt", 'w')
list=["Ramesh\n" ,"Arjun\n", "Senthil\n", "Vignesh"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()

