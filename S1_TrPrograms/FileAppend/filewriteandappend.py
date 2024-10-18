with open("text.txt","w") as file:
    file.write("I am learning Python!\n")
    file.write("I am really enjoying it!\n")
    file.write("And I want to add more lines to say how much I like it")
with open("text.txt","a") as file:
    file.write("What I want to add on goes here")
with  open('text.txt','r') as file:
    print(file.read())
file.close()
