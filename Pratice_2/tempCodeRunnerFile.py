network_db={"Router1":{"name":"Router1","IP":"192.268.2.34","username":"KKH","pwd":"123"}}


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
print(network_db)
print("--------------------------------------------------------------------------------------------")