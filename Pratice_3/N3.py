with open("Cinderella.txt","r")as f:
    content=f.read()
word_to_search = "Cinderella"

count=content.count(word_to_search)

print(f"Word_Count:{count}")