no_of_pairs=int(input())
d=dict()
for i in range(no_of_pairs):
    key=int(input())
    value=input()
    d[key]=value
K=int(input())

#Type 1

if K in d.keys():
    print("Key exist")
else:
    print("Key doesn't exist")

#Type 2

if K in d:
    print("Key exist")
else:
    print("Key does'nt exist")

#Type 3

try:
    key=d[K]
    print("Key Exist")
except:
    print("Key doesn't exist")
    
    

