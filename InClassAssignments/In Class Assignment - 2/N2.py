string=input("Enter the long string :")#eatbatsatfatratranif
end=int(input("Enter the number in each part:"))

str_length=len(string)
start=0
temp=end

while (end <= str_length):
 
 print(string[start:end])
 start=end
 end=end+temp

 if (end > str_length):
   print(string[start:])

