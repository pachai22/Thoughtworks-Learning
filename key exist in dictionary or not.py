no_of_pairs=int(input())
dictionary=dict()
for i in range(no_of_pairs):
    key=int(input())
    value=input()
    dictionary[key]=value
find_key=int(input())

#Type 1

if find_key in dictionary.keys():
    print("Key exist")
else:
    print("Key doesn't exist")

#Type 2

if find_key in dictionary:
    print("Key exist")
else:
    print("Key does'nt exist")

#Type 3

try:
    key=dictionary[find_key]
    print("Key Exist")
except:
    print("Key doesn't exist")
    
    

