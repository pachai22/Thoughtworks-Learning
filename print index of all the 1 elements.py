l=[1,2,4,5,1,1,4,1,56]
#Type 1

ans=[]
for i in range(len(l)):
    if l[i]==1:
        ans.append(i)
print(ans)

#Type 2

ans=[i for i in range(len(l)) if l[i]==1]
print(ans)

#Type 3
ans=[index for index,value in enumerate(l) if value==1]
print(ans)

#Type 4
ans=list(filter(lambda i : l[i]==1,range(len(l))))
print(ans)


