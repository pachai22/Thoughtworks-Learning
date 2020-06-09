list1=[1,2,4,5,1,1,4,1,56]
#Type 1

indices=[]
for i in range(len(list1)):
    if list1[i]==1:
        indices.append(i)
print(indices)

#Type 2

indices=[i for i in range(len(list1)) if list1[i]==1]
print(indices)

#Type 3
indices=[index for index,value in enumerate(list1) if value==1]
print(indices)

#Type 4
indices=list(filter(lambda i : list1[i]==1,range(len(list1))))
print(indices)


