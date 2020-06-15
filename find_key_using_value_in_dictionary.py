

given_dictionary = {'Spain':'Europe','Japan':'Asia','India':'Asia','Italy':'Europe','Thailand':'Asia','Sudan':'Africa'}
print("Please select any continent from this :",set(given_dictionary.values()))
desired_continent = input("Desired continent :")

print("The countries are :",end=" ")
for key,value in given_dictionary.items():
    if value.lower() == desired_continent.lower() :
        print(key,end=" ")


'''Input :

 Desired continent :Europe

 Output :

 Spain Italy

 Input :

 Desired continent :Africa

 Output :

 Sudan

 '''
        
        
