from teacher import Teacher

t=Teacher()

t.setid(10)
t.setname("Prakash")
t.setsalary(25000)
t.setaddress("HNO-10, Rajouri gardens, Delhi")

print("ID: ",t.getid())
print("Name: ",t.getname())
print("Salary: ",t.getsalary())
print("Address: ",t.getaddress())
