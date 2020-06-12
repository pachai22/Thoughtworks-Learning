

given_dictionary = {'Spain':'Europe','Japan':'Asia','India':'Asia','Italy':'Europe','Thailand':'Asia','Sudan':'Africa'}

desired_continent = input("Desired continent :")


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
        
        
