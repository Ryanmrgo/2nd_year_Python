def student(name,**info):
    
        print("Name=",name)
        
        for x,y in info.items():
             print(x,y)

student("Mg Sanda Pyae Sone",roll_number="2021_MIIT_CSE_061",CSE_IV="A",CSE_V="A")   