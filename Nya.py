vowels = {"Ня":"На","Ня":"но","я":"а","ль":"л"}
def nya(text):
    for i in vowels:
        text =text.replace(vowels[i],i)
    return text
    
    
