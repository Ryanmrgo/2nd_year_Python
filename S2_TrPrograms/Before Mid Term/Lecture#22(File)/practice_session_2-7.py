network_db={1:{"name":"Router1","IP":"192.168.2.34","username":"KKH","pwd":"123"}}
for k,v in network_db.items():
    print(k)
    print(v)
    #print(network_db[1].get('name'))

#check whether the Router2 is present
usename=input("Enter TP Link Router Name:")

if usename == network_db[1].get('name'):
    print("Router is exist!",network_db[1].get('name'))

else:
    print("Router2 is not exist!")
    name=input("Enter TP Link Router Name:")
    IP=input("Enter IP: ")
    username=input("Enter username: ")
    pwd=input("Enter password : ")
    network_db.update({2:{"name":name,"IP":IP,"username":username,"pwd":pwd}})
    #print("Updated router data in network_db : ",network_db.items())

    print("Updated router data in network_db : ")
    for k,v in network_db.items():
        print(v)


