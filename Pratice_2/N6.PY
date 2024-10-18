
favorite_languages = {
    'Zezawar': ['Python', 'Ruby'],
    'Kay Kay': ['C'],
    'Aung Aung': ['Ruby', 'Go'],
    'Aye Aye': ['Python', 'Haskell']
}


for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name}'s favorite language is:")
    else:
        print(f"{name}'s favorite languages are:")
    
    for i in languages:
        print(i)
    
    print()  
