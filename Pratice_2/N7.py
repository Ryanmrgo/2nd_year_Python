
'''network_db={"Router1":{"name":"Router1","IP":"192.268.2.34","username":"KKH","pwd":"123"}}


def print_database(database):
    for router,attribute in database.items():
        print(f"{router} details:")
        for key,value in database.items():
            print(f"{key}:{value}")
        print()


print("--------------------------------------------------------------------------------------------")
print("Inital Data Base:")
print_database(network_db)
print("--------------------------------------------------------------------------------------------")
router2_name="Router2"

if router2_name in network_db:
    print(f"{router2_name} details:")
    print_database(network_db[router2_name])
else :
    network_db[router2_name]={'name': router2_name, 'IP': '192.168.431', 'username': 'SDPS', 'pwd': '456'}
    print("Router2 does not exist.")
    print("Router2 added to the database with default values.")
print("--------------------------------------------------------------------------------------------")
print("\nUpadated network database:")
print_database(network_db)
print(network_db["Router1"])
print(network_db["Router2"])

print("--------------------------------------------------------------------------------------------")
'''

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
