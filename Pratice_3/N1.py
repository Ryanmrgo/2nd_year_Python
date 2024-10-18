# with open ("myanmartext.txt","w")as f:
#     lines=[" ယနေေ့နေသာသည်။","ပန်းကလေးများဖူးပွင့်နေ့ကြသည်။","ခရေပန်းကလေးများကြွေကျနေသည်"]
#     f.write('\n'.join(lines))


# with open('myanmartext.txt', 'r', encoding='utf-8') as f:
#     read_sentences = f.readlines()

# for sentence in read_sentences:
#     print(sentence.strip())   
#     
# # Writing sentences to a file
# with open('myanmartext.txt', 'w', encoding='utf-8') as file:
#     sentences = [
#         "ယနေေ့နေသာသည်။","ပန်းကလေးများဖူးပွင့်နေ့ကြသည်။","ခရေပန်းကလေးများကြွေကျနေသည်"
#     ]
#     file.write('\n'.join(sentences))

# # Reading and printing sentences from the file
# try:
#     with open('myanmartext.txt', 'r', encoding='utf-8') as file:
#         read_sentences = file.readlines()

#     for sentence in read_sentences:
#         print(sentence.strip())
# except UnicodeEncodeError:
#     print("Unable to print Unicode characters to console. Please check the output in the 'myanmartext.txt' file.")


with open("myanmartext.txt","w",encoding='utf-8')as f:
      sentence="ယနေေ့နေသာသည်။\nပေ််း ကန ်း မ ာ်း ဖ ်း ပွငေ့်နေကကသည်။\nခနေပေ််း န ်း မ ာ်း ကနပမပပင်သေ့န ကက နေသည်။"
      f.write(sentence)

with open("myanmartext.txt", 'r', encoding='utf-8') as f:
       read_sentences = f.read()
       print(read_sentences.strip())
      
    
          