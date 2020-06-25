import re
string=input("Enter the String :")
string1=input("Enter the String2 :")
string=re.sub(r"\s","",string)
string1=re.sub(r"\s","",string1)
string=list(string)
string1=list(string1)

if len(string)==len(string1) :
    for i in range(len(string)):
        for j in range(len(string1)):
            if string[i]==string1[j]: 
                string1[j]=" "
                break
    if not " ".join(string1).isalpha():
        print("Anagram")
    else:
        print("Not an anagram")
                
else:
        print("Not an anagram")
